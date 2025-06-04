// Arquivo de configuração para o dashboard
const config = {
  // Configuração da API do Google Sheets
  googleSheets: {
    sheetId: '1TOAFgcacj6FbZk_sD5O6engaw1Y6UPyR7m59UCjm8Z4',
    sheetName: 'Sheet1', // Nome da aba pode precisar ser ajustado
    apiKey: 'https://sheetdb.io/api/v1/8fgezuudv2776' // Será configurado pelo usuário
  },
  
  // Configuração usando SheetDB (recomendado)
  sheetDB: {
    apiUrl: '' // URL da API SheetDB a ser configurada pelo usuário
  },
  
  // Configurações de visualização
  display: {
    dateFormat: 'DD/MM/YYYY',
    currencyFormat: 'pt-BR',
    maxPendingItems: 10,
    refreshInterval: 0 // 0 = apenas manual, ou definir em milissegundos
  }
};
