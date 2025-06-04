// Arquivo de configuração para o dashboard
window.config = {
    // Configuração da API do Google Sheets (não usada diretamente, mas mantida caso seja necessário no futuro)
    googleSheets: {
      sheetId: '1TOAFgcacj6FbZk_sD5O6engaw1Y6UPyR7m59UCjm8Z4',
      sheetName: 'Sheet1',
      apiKey: 'AIzaSyDr1HOQkxfzdWRDniFX_M1kQXvRS2xYwhI'
    },
    
    // URL da API SheetDB gerada para conectar ao Google Sheets
    sheetDB: {
      apiUrl: 'https://sheetdb.io/api/v1/8fgezuudv2776'
    },
    
    // Configurações de exibição do dashboard
    display: {
      dateFormat: 'DD/MM/YYYY',
      currencyFormat: 'pt-BR',
      maxPendingItems: 10,
      refreshInterval: 0 // 0 = atualização somente ao clicar no botão
    }
  };
  