# Documentação do Dashboard Financeiro Aprimorado

## Visão Geral

Este dashboard financeiro responsivo foi desenvolvido para oferecer uma visualização interativa e detalhada de dados financeiros, com recursos avançados de filtragem e análise. O dashboard inclui:

1. **Filtro de data de pagamento** - Permite filtrar os dados por período específico
2. **Interatividade nos números** - Ao clicar nos valores/números, o dashboard filtra e seleciona os itens correspondentes
3. **Análise por serviços** - Visualização específica para análise por tipo de serviço
4. **Design responsivo** - Funciona em qualquer dispositivo (desktop, tablet ou celular)
5. **Botão de atualização manual** - Permite buscar os dados mais recentes quando desejar

## Arquivos Incluídos

- `dashboard_enhanced.html` - O arquivo principal do dashboard com interface responsiva e recursos avançados
- `config.js` - Arquivo de configuração para integração com SheetDB
- `README.md` - Este arquivo de documentação

## Novas Funcionalidades

### 1. Filtro de Data de Pagamento
- Permite selecionar um intervalo de datas para filtrar os pagamentos
- Utiliza um seletor de data intuitivo com calendário visual
- Os filtros ativos são exibidos como badges que podem ser removidos individualmente

### 2. Interatividade nos Cards e Gráficos
- Clique nos cards de resumo para filtrar por categoria, serviço ou status
- Clique nos elementos dos gráficos para filtrar os dados correspondentes
- Os elementos filtrados são destacados visualmente na tabela de pagamentos

### 3. Análise por Serviços
- Nova visualização dedicada à análise por tipo de serviço
- Gráfico de barras horizontais para melhor visualização dos serviços
- Integração com os filtros existentes para análise cruzada

### 4. Sistema de Navegação por Abas
- Interface organizada em abas para facilitar a navegação entre diferentes visualizações
- Transição suave entre as visualizações de despesas mensais, categorias e serviços

## Instruções de Implantação

### 1. Configurar o SheetDB

Para conectar seu Google Sheets ao dashboard:

1. Acesse [SheetDB.io](https://sheetdb.io/) e crie uma conta gratuita
2. Clique em "Create New API"
3. Cole o URL do seu Google Sheets: `https://docs.google.com/spreadsheets/d/1TOAFgcacj6FbZk_sD5O6engaw1Y6UPyR7m59UCjm8Z4/edit`
4. Certifique-se de que seu Google Sheets está configurado para "Qualquer pessoa com o link pode visualizar"
5. Copie a URL da API gerada pelo SheetDB

### 2. Atualizar o arquivo config.js

Abra o arquivo `config.js` e atualize com a URL da API do SheetDB:

```javascript
// Arquivo de configuração para o dashboard
const config = {
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
2. Faça upload dos arquivos: `dashboard_enhanced.html` (renomeado para `index.html`), `config.js` e qualquer outro arquivo necessário
3. Vá para Settings > Pages
4. Em "Source", selecione "main" e clique em "Save"
5. Aguarde alguns minutos e seu dashboard estará disponível no URL fornecido

## Requisitos da Planilha

Para que o dashboard funcione corretamente, sua planilha do Google Sheets deve conter as seguintes colunas:

- `Descrição` - Descrição do pagamento
- `Valor Pagamento` - Valor do pagamento (formato numérico ou texto com R$)
- `Categoria` - Categoria do pagamento
- `Fornecedor` - Nome do fornecedor
- `Serviço` - Tipo de serviço (nova coluna necessária)
- `Vencimento` - Data de vencimento (formato DD/MM/YYYY)
- `Data Pagamento` - Data em que o pagamento foi realizado (formato DD/MM/YYYY)
- `status do pagamento` - Status do pagamento (ex: "Pago", "Em Aberto")
- `Mes de Vencimento` - Mês de vencimento (formato MM/YYYY)

## Uso do Dashboard

### Filtros
- **Filtro de Data**: Clique no campo de data para selecionar um intervalo
- **Filtros por Card**: Clique nos cards de resumo para filtrar por categoria, serviço ou status
- **Filtros por Gráfico**: Clique nos elementos dos gráficos para filtrar os dados correspondentes
- **Limpar Filtros**: Use o botão "Limpar Filtros" para remover todos os filtros ativos

### Navegação
- Use as abas para alternar entre diferentes visualizações
- A tabela de pagamentos sempre mostra os dados filtrados atualmente
- Os elementos filtrados são destacados visualmente na tabela

### Atualização de Dados
- Clique no botão "Atualizar Dados" para buscar os dados mais recentes do Google Sheets
- O timestamp da última atualização é exibido ao lado do botão

## Personalização

Você pode personalizar o dashboard editando:

- O arquivo `config.js` para ajustar configurações de exibição
- O arquivo HTML para modificar o layout ou adicionar novas visualizações
- Os estilos CSS para alterar cores, fontes e outros elementos visuais

## Suporte

Para dúvidas ou problemas, entre em contato com o desenvolvedor.
