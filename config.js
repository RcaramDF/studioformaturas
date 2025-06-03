// config.js

// Definindo o objeto global “config” para que o dashboard o leia corretamente
window.config = {
  // Como usaremos apenas SheetDB aqui, deixamos todas as chaves de googleSheets vazias:
  googleSheets: {
    sheetId:   '',
    sheetName: '',
    apiKey:    ''
  },

  // Cole aqui a URL exatamente como o SheetDB forneceu (sem ficar repetindo o sheetId)
  sheetDB: {
    apiUrl: 'https://sheetdb.io/api/v1/cwfixe9vilf6z'
  },

  // Configurações de formatação e comportamento do dashboard
  display: {
    dateFormat:      'DD/MM/YYYY',
    currencyFormat:  'pt-BR',
    maxPendingItems: 10,
    refreshInterval: 0   // 0 = só carregamento manual ao clicar em “Atualizar Dados”
  }
};
