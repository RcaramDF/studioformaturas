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

# Criar gráficos individuais e depois combiná-los em um HTML

# 1. Gráfico de Despesas Mensais (Gráfico de Barras)
monthly_expenses = df.groupby('Mes_Vencimento')['Valor Pagamento'].sum().reset_index()
monthly_expenses = monthly_expenses.sort_values(by='Mes_Vencimento')

fig_monthly = px.bar(
    monthly_expenses, 
    x='Mes_Vencimento', 
    y='Valor Pagamento',
    title='Despesas Mensais',
    labels={'Mes_Vencimento': 'Mês', 'Valor Pagamento': 'Valor (R$)'},
    text_auto='.2s',
    height=400
)
fig_monthly.update_traces(
    texttemplate='R$ %{y:.2f}',
    textposition='outside',
    marker_color='rgb(55, 83, 109)'
)
fig_monthly.update_layout(template='plotly_white')

# 2. Gráfico de Gastos por Categoria (Gráfico de Pizza)
category_expenses = df.groupby('Categoria')['Valor Pagamento'].sum().reset_index()
category_expenses = category_expenses.sort_values(by='Valor Pagamento', ascending=False)

fig_category = px.pie(
    category_expenses,
    values='Valor Pagamento',
    names='Categoria',
    title='Gastos por Categoria',
    hole=0.4,
    height=500
)
fig_category.update_traces(textinfo='label+percent')
fig_category.update_layout(template='plotly_white')

# 3. Tabela de Pagamentos Pendentes
pending_payments = df[df['status do pagamento'] != 'Pago'].sort_values(by='Vencimento')
pending_table = pending_payments[['Descrição', 'Fornecedor', 'Vencimento', 'Valor Pagamento', 'status do pagamento']].head(10)

# Formatar valores para exibição
pending_table['Vencimento'] = pending_table['Vencimento'].dt.strftime('%d/%m/%Y')
pending_table['Valor_Formatado'] = pending_table['Valor Pagamento'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

fig_pending = go.Figure(
    data=[go.Table(
        header=dict(
            values=['Descrição', 'Fornecedor', 'Vencimento', 'Valor', 'Status'],
            fill_color='rgb(55, 83, 109)',
            align='left',
            font=dict(color='white', size=12)
        ),
        cells=dict(
            values=[
                pending_table['Descrição'],
                pending_table['Fornecedor'],
                pending_table['Vencimento'],
                pending_table['Valor_Formatado'],
                pending_table['status do pagamento']
            ],
            fill_color='lavender',
            align='left',
            font=dict(size=11)
        )
    )]
)
fig_pending.update_layout(
    title='Pagamentos Pendentes',
    template='plotly_white',
    height=400
)

# Salvar os gráficos individuais como HTML
fig_monthly.write_html('/home/ubuntu/grafico_despesas_mensais.html')
fig_category.write_html('/home/ubuntu/grafico_categorias.html')
fig_pending.write_html('/home/ubuntu/tabela_pendentes.html')

# Criar um arquivo HTML completo com os três gráficos
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
                    <div id="grafico-despesas-mensais"></div>
                </div>
            </div>
        </div>
        
        <div class="row">
            <div class="col-lg-6">
                <div class="graph-container">
                    <div id="grafico-categorias"></div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="graph-container">
                    <div id="tabela-pendentes"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Carregar os gráficos individuais
        fetch('grafico_despesas_mensais.html')
            .then(response => response.text())
            .then(html => {{
                const div = document.createElement('div');
                div.innerHTML = html;
                const plotlyDiv = div.querySelector('.plotly-graph-div');
                document.getElementById('grafico-despesas-mensais').appendChild(plotlyDiv);
            }});
            
        fetch('grafico_categorias.html')
            .then(response => response.text())
            .then(html => {{
                const div = document.createElement('div');
                div.innerHTML = html;
                const plotlyDiv = div.querySelector('.plotly-graph-div');
                document.getElementById('grafico-categorias').appendChild(plotlyDiv);
            }});
            
        fetch('tabela_pendentes.html')
            .then(response => response.text())
            .then(html => {{
                const div = document.createElement('div');
                div.innerHTML = html;
                const plotlyDiv = div.querySelector('.plotly-graph-div');
                document.getElementById('tabela-pendentes').appendChild(plotlyDiv);
            }});
    </script>
</body>
</html>
"""

# Salvar o HTML completo
with open('/home/ubuntu/dashboard_financeiro_v2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Dashboard versão 2 criado com sucesso!")
