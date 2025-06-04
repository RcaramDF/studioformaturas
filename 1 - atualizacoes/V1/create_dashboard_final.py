import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import re

# Função para limpar valores monetários
def clean_currency(x):
    if isinstance(x, str):
        return float(x.replace('R$', '').replace('.', '').replace(',', '.').strip() or 0)
    return float(x or 0)

# Função para converter datas
def parse_date(date_str):
    if pd.isna(date_str):
        return None
    try:
        return pd.to_datetime(date_str, format='%d/%m/%y')
    except:
        try:
            return pd.to_datetime(date_str, format='%d/%m/%Y')
        except:
            return None

# Carregar os dados
df = pd.read_csv('/home/ubuntu/dashboard_data.csv')

# Limpeza e preparação dos dados
# Converter colunas monetárias
monetary_cols = ['Valor Parcela', 'Total Conta', 'Valor Pagamento', 'Valor Multa', 'Valor Juros', 'Valor Desconto', 'Impostos']
for col in monetary_cols:
    if col in df.columns:
        df[col] = df[col].apply(clean_currency)

# Converter datas
date_cols = ['Vencimento', 'Pagamento']
for col in date_cols:
    if col in df.columns:
        df[col] = df[col].apply(parse_date)

# Extrair mês e ano das datas
df['Mes_Vencimento'] = df['Vencimento'].dt.strftime('%m/%Y')
df['Ano_Vencimento'] = df['Vencimento'].dt.year
df['Mes_Num_Vencimento'] = df['Vencimento'].dt.month

# 1. Gráfico de Despesas Mensais (Gráfico de Barras)
monthly_expenses = df.groupby('Mes_Vencimento')['Valor Pagamento'].sum().reset_index()
monthly_expenses = monthly_expenses.sort_values(by='Mes_Vencimento')

# 2. Gráfico de Gastos por Categoria (Gráfico de Pizza)
category_expenses = df.groupby('Categoria')['Valor Pagamento'].sum().reset_index()
category_expenses = category_expenses.sort_values(by='Valor Pagamento', ascending=False)

# 3. Tabela de Pagamentos Pendentes
pending_payments = df[df['status do pagamento'] != 'Pago'].sort_values(by='Vencimento')
pending_table = pending_payments[['Descrição', 'Fornecedor', 'Vencimento', 'Valor Pagamento', 'status do pagamento']].head(10)

# Formatar valores para exibição na tabela
pending_table_display = pending_table.copy()
pending_table_display['Vencimento'] = pending_table_display['Vencimento'].dt.strftime('%d/%m/%Y')
pending_table_display['Valor_Formatado'] = pending_table_display['Valor Pagamento'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

# Criar HTML com os gráficos incorporados diretamente
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Financeiro</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .dashboard-container {{
            max-width: 1400px;
            margin: 0 auto;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            padding: 20px;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }}
        .header h1 {{
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        .header p {{
            color: #7f8c8d;
            font-size: 1.1em;
        }}
        .dashboard-summary {{
            display: flex;
            justify-content: space-around;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }}
        .summary-card {{
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 20px;
            width: 30%;
            min-width: 250px;
            margin-bottom: 20px;
            border-left: 5px solid;
        }}
        .total-expenses {{
            border-left-color: #3498db;
        }}
        .pending-payments {{
            border-left-color: #e74c3c;
        }}
        .top-category {{
            border-left-color: #2ecc71;
        }}
        .summary-card h3 {{
            margin-top: 0;
            color: #34495e;
            font-size: 1.2em;
        }}
        .summary-card p {{
            font-size: 1.8em;
            font-weight: bold;
            margin: 10px 0 0;
        }}
        .summary-card .subtitle {{
            font-size: 0.9em;
            color: #95a5a6;
            margin: 5px 0 0;
        }}
        .graph-container {{
            margin-bottom: 30px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 15px;
        }}
        .row {{
            display: flex;
            flex-wrap: wrap;
            margin-right: -15px;
            margin-left: -15px;
        }}
        .col-md-12, .col-lg-6 {{
            padding-right: 15px;
            padding-left: 15px;
            width: 100%;
        }}
        @media (min-width: 992px) {{
            .col-lg-6 {{
                width: 50%;
            }}
        }}
        @media (max-width: 768px) {{
            .summary-card {{
                width: 100%;
            }}
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: rgb(55, 83, 109);
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: lavender;
        }}
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="header">
            <h1>Dashboard Financeiro</h1>
            <p>Acompanhamento de despesas, categorias e pagamentos pendentes</p>
        </div>
        
        <div class="dashboard-summary">
            <div class="summary-card total-expenses">
                <h3>Total de Despesas</h3>
                <p>R$ {df['Valor Pagamento'].sum():,.2f}</p>
                <div class="subtitle">Valor total de todas as despesas</div>
            </div>
            
            <div class="summary-card pending-payments">
                <h3>Pagamentos Pendentes</h3>
                <p>{len(df[df['status do pagamento'] != 'Pago'])}</p>
                <div class="subtitle">Número de pagamentos não realizados</div>
            </div>
            
            <div class="summary-card top-category">
                <h3>Categoria Principal</h3>
                <p>{category_expenses.iloc[0]['Categoria']}</p>
                <div class="subtitle">R$ {category_expenses.iloc[0]['Valor Pagamento']:,.2f}</div>
            </div>
        </div>
        
        <div class="row">
            <div class="col-md-12">
                <div class="graph-container">
                    <h3>Despesas Mensais</h3>
                    <div id="grafico-despesas-mensais" style="height: 400px;"></div>
                </div>
            </div>
        </div>
        
        <div class="row">
            <div class="col-lg-6">
                <div class="graph-container">
                    <h3>Gastos por Categoria</h3>
                    <div id="grafico-categorias" style="height: 500px;"></div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="graph-container">
                    <h3>Pagamentos Pendentes</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Descrição</th>
                                <th>Fornecedor</th>
                                <th>Vencimento</th>
                                <th>Valor</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
"""

# Adicionar linhas da tabela de pagamentos pendentes
for _, row in pending_table_display.iterrows():
    html_content += f"""
                            <tr>
                                <td>{row['Descrição'] if not pd.isna(row['Descrição']) else ''}</td>
                                <td>{row['Fornecedor']}</td>
                                <td>{row['Vencimento']}</td>
                                <td>{row['Valor_Formatado']}</td>
                                <td>{row['status do pagamento']}</td>
                            </tr>
    """

# Continuar o HTML com os scripts para os gráficos
html_content += f"""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Gráfico de Despesas Mensais
        var monthlyData = {{
            x: {monthly_expenses['Mes_Vencimento'].tolist()},
            y: {monthly_expenses['Valor Pagamento'].tolist()},
            text: {[f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') for x in monthly_expenses['Valor Pagamento'].tolist()]},
            type: 'bar',
            marker: {{
                color: 'rgb(55, 83, 109)'
            }},
            textposition: 'auto'
        }};

        var monthlyLayout = {{
            title: '',
            xaxis: {{
                title: 'Mês'
            }},
            yaxis: {{
                title: 'Valor (R$)'
            }},
            template: 'plotly_white'
        }};

        Plotly.newPlot('grafico-despesas-mensais', [monthlyData], monthlyLayout);

        // Gráfico de Gastos por Categoria
        var categoryData = {{
            values: {category_expenses['Valor Pagamento'].tolist()},
            labels: {category_expenses['Categoria'].tolist()},
            type: 'pie',
            hole: 0.4,
            textinfo: 'label+percent',
            insidetextorientation: 'radial'
        }};

        var categoryLayout = {{
            title: '',
            template: 'plotly_white'
        }};

        Plotly.newPlot('grafico-categorias', [categoryData], categoryLayout);
    </script>
</body>
</html>
"""

# Salvar o HTML completo
with open('/home/ubuntu/dashboard_financeiro_final.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Dashboard final criado com sucesso!")
