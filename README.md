# Currency Rate Checker 🌎💱

Script em Python que consulta cotações de pares de moedas em tempo real usando a [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas).  
O usuário informa os pares desejados (por exemplo: `usd-brl,usd-jpy`), e o programa retorna as informações de cada par.

> ⚠️ Projeto em construção — novas funcionalidades serão adicionadas.

## 📌 Funcionalidades atuais
- Recebe múltiplos pares de moedas separados por vírgulas
- Consulta a API da AwesomeAPI em tempo real
- Trata caso de pares invertidos (ex.: `brl-usd` → `usd-brl`)
- Exibe os dados retornados pela API no formato JSON

## 🚀 Tecnologias
- Python 3.10+
- Biblioteca [requests](https://pypi.org/project/requests/)

## ▶️ Como usar
1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/The-Darkar/currency-rate-checker.git
   cd currency-rate-checker
.
