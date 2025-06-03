// config.js

window.config = {
  // Usaremos apenas SheetDB, então as chaves de googleSheets ficam vazias:
  googleSheets: {
    sheetId:   '',
    sheetName: '',
    apiKey:    ''
  },

  // Cole aqui a URL da API que o SheetDB gerou para você:
  sheetDB: {
    apiUrl: 'https://sheetdb.io/api/v1/8fgezuudv2776'
  },

  // Configurações de exibição do dashboard
  display: {
    dateFormat:      'DD/MM/YYYY',
    currencyFormat:  'pt-BR',
    maxPendingItems: 10,
    refreshInterval: 0   // 0 = atualização somente ao clicar no botão
  }
};
