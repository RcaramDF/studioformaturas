# Dashboard Financeiro Responsivo

Este projeto consiste em um dashboard financeiro responsivo com botão de atualização manual, que permite visualizar dados de despesas, categorias e pagamentos pendentes a partir de uma planilha do Google Sheets.

## Arquivos Incluídos

- `dashboard_final.html`: O arquivo principal do dashboard com interface responsiva

- `config.js`: Arquivo de configuração para integração com SheetDB

- `README.md`: Este arquivo de documentação

## Instruções de Implantação

### 1. Configurar o SheetDB

Para conectar seu Google Sheets ao dashboard:

1. Acesse [SheetDB.io](https://sheetdb.io/) e crie uma conta gratuita

1. Clique em "Create New API"

1. Cole o URL do seu Google Sheets: `https://docs.google.com/spreadsheets/d/1TOAFgcacj6FbZk_sD5O6engaw1Y6UPyR7m59UCjm8Z4/edit`

1. Certifique-se de que seu Google Sheets está configurado para "Qualquer pessoa com o link pode visualizar"

1. Copie a URL da API gerada pelo SheetDB

### 2. Atualizar o arquivo config.js

Abra o arquivo `config.js` e atualize com a URL da API do SheetDB:

```javascript
// Arquivo de configuração para o dashboard
const config = {
  // Configuração da API do Google Sheets
  googleSheets: {
    sheetId: '1TOAFgcacj6FbZk_sD5O6engaw1Y6UPyR7m59UCjm8Z4',
    sheetName: 'Sheet1', // Nome da aba pode precisar ser ajustado
    apiKey: '' // Não é necessário com SheetDB
  },
  
  // Configuração usando SheetDB (recomendado)
  sheetDB: {
    apiUrl: 'SUA_URL_DA_API_SHEETDB_AQUI'
  },
  
  // Configurações de visualização
  display: {
    dateFormat: 'DD/MM/YYYY',
    currencyFormat: 'pt-BR',
    maxPendingItems: 10,
    refreshInterval: 0 // 0 = apenas manual
  }
};
```

### 3. Hospedar no GitHub Pages

Para disponibilizar o dashboard online:

1. Crie um repositório no GitHub

1. Faça upload dos arquivos: `dashboard_final.html` (renomeado para `index.html`), `config.js` e qualquer outro arquivo necessário

1. Vá para Settings > Pages

1. Em "Source", selecione "main" e clique em "Save"

1. Aguarde alguns minutos e seu dashboard estará disponível no URL fornecido (geralmente `https://seu-usuario.github.io/nome-do-repositorio`)

### 4. Alternativas de Hospedagem

Além do GitHub Pages, você pode hospedar o dashboard em:

- **Netlify**: Faça upload dos arquivos ou conecte ao seu repositório GitHub

- **Vercel**: Conecte ao seu repositório GitHub para implantação automática

- **Firebase Hosting**: Use o Firebase CLI para implantar os arquivos

## Uso do Dashboard

1. Acesse o dashboard através do URL de hospedagem

1. Os dados de demonstração serão carregados inicialmente

1. Clique no botão "Atualizar Dados" para buscar os dados reais do seu Google Sheets

1. O dashboard exibirá:
  - Total de despesas
  - Número de pagamentos pendentes
  - Categoria principal de gastos
  - Gráfico de despesas mensais
  - Gráfico de gastos por categoria
  - Tabela de pagamentos pendentes

## Personalização

Você pode personalizar o dashboard editando:

- O arquivo `config.js` para ajustar configurações de exibição

- O arquivo HTML para modificar o layout ou adicionar novas visualizações

- Os estilos CSS para alterar cores, fontes e outros elementos visuais

## Limitações

- O dashboard requer conexão com internet para atualizar os dados

- A atualização é manual (clique no botão) e não automática

- O SheetDB tem limites de requisições no plano gratuito (1000 requisições/mês)

## Suporte

Para dúvidas ou problemas, entre em contato com o desenvolvedor.

