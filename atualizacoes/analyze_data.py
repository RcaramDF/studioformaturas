import pandas as pd

def analyze_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Arquivo lido com sucesso: {file_path}")
        print("\nInformações do DataFrame:")
        df.info()
        print("\nPrimeiras 5 linhas:")
        print(df.head().to_markdown(index=False))
        print("\nTipos de dados por coluna:")
        print(df.dtypes)
        print("\nValores ausentes por coluna:")
        print(df.isnull().sum())
        print("\nEstatísticas descritivas (colunas numéricas):")
        # Tentar converter colunas de moeda para numérico antes de descrever
        currency_cols = ['Valor Parcela', 'Total Conta', 'Valor Pagamento', 'Valor Multa', 'Valor Juros', 'Valor Desconto', 'Impostos']
        for col in currency_cols:
            if col in df.columns:
                # Remover 'R$ ', converter ',' para '.' e depois para numérico
                df[col] = df[col].astype(str).str.replace('R$', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.', regex=False).str.strip()
                # Tentar converter para numérico, tratando erros
                df[col] = pd.to_numeric(df[col], errors='coerce')
        print(df.describe().to_markdown())

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {file_path}")
    except Exception as e:
        print(f"Ocorreu um erro ao analisar o CSV: {e}")

analyze_csv('/home/ubuntu/dashboard_data.csv')
