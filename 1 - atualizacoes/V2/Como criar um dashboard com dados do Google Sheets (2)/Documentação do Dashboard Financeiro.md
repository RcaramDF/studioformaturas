# Documentação do Dashboard Financeiro

## Visão Geral

Este dashboard financeiro foi desenvolvido para fornecer uma visão completa e interativa das finanças, com foco em contas a pagar. O sistema permite visualizar valores pagos, em aberto a vencer, vencidos, além de análises gráficas e listas detalhadas de pagamentos.

## Funcionalidades Principais

1. **Visão Geral Financeira**
   - Cards com valores totais pagos, a vencer, vencidos e total geral
   - Atualização dinâmica conforme filtros aplicados

2. **Análises Gráficas**
   - Gráfico de colunas mensal com valores de pagamentos
   - Gráfico de disco (pizza) mostrando proporção entre valores pagos, vencidos e a vencer

3. **Listas de Pagamentos**
   - Pagamentos vencidos
   - Pagamentos a vencer
   - Pagamentos já realizados

4. **Sistema de Filtros**
   - Filtro por período de pagamento
   - Filtros interativos ao clicar em cards, gráficos e listas
   - Visualização de filtros ativos e opção para limpar

5. **Menu de Navegação**
   - Dashboard principal
   - Contas a pagar
   - Contas a receber (preparado para implementação futura)
   - Relatórios
   - Configurações

## Interatividade

O dashboard é totalmente interativo, permitindo:

- Clicar nos cards para filtrar por status (pago, a vencer, vencido)
- Clicar nas colunas do gráfico mensal para filtrar por mês
- Clicar nas fatias do gráfico de pizza para filtrar por status
- Clicar em itens das listas para filtrar por categoria ou serviço
- Selecionar períodos específicos no filtro de datas
- Limpar filtros individualmente ou todos de uma vez

## Requisitos Técnicos

### Para Visualização
- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Conexão com internet para carregamento das bibliotecas

### Para Implantação
- Servidor web para hospedar os arquivos HTML/CSS/JS
- Conta no SheetDB para conexão com Google Sheets (opcional)

## Guia de Implantação

### Opção 1: Implantação via GitHub Pages

1. Crie uma conta no GitHub (se ainda não tiver)
2. Crie um novo repositório
3. Faça upload dos arquivos do dashboard:
   - `dashboard_new_layout_implemented.html` (renomeie para `index.html`)
   - `config_enhanced.js` (renomeie para `config.js`)
4. Acesse as configurações do repositório e ative o GitHub Pages
5. O dashboard estará disponível em `https://seu-usuario.github.io/seu-repositorio`

### Opção 2: Implantação em Servidor Web Próprio

1. Faça upload dos arquivos para seu servidor web:
   - `dashboard_new_layout_implemented.html` (renomeie para `index.html`)
   - `config_enhanced.js` (renomeie para `config.js`)
2. Configure o servidor para servir os arquivos estáticos
3. Acesse o dashboard pelo endereço do seu servidor

## Conexão com Dados Reais

Para conectar o dashboard aos seus dados reais do Google Sheets:

1. Acesse [SheetDB.io](https://sheetdb.io/) e crie uma conta gratuita
2. Conecte sua planilha do Google Sheets seguindo as instruções do site
3. Copie a URL da API gerada
4. Edite o arquivo `config.js` e substitua o valor de `apiUrl` pela URL da sua API

## Estrutura de Dados Necessária

Sua planilha do Google Sheets deve conter as seguintes colunas:

- `Descrição`: Descrição do pagamento
- `Valor Pagamento`: Valor do pagamento (formato: R$ 0,00)
- `Categoria`: Categoria do pagamento
- `Fornecedor`: Nome do fornecedor
- `Serviço`: Tipo de serviço
- `Vencimento`: Data de vencimento (formato: DD/MM/YYYY)
- `Data Pagamento`: Data em que o pagamento foi realizado (formato: DD/MM/YYYY)
- `status do pagamento`: Status do pagamento (ex: "Pago", "Em Aberto")
- `Mes de Vencimento`: Mês de vencimento (formato: MM/YYYY)

## Personalização

### Cores e Estilo

Para personalizar as cores do dashboard, edite as variáveis CSS no início do arquivo HTML ou modifique as configurações de cores no arquivo `config.js`.

### Layout

O layout é responsivo e se adapta automaticamente a diferentes tamanhos de tela. Para ajustes mais específicos, modifique as classes CSS no arquivo HTML.

## Suporte e Manutenção

Para atualizações ou suporte adicional, entre em contato com o desenvolvedor.

---

© 2025 Dashboard Financeiro - Todos os direitos reservados
