#Consultar API e retornar valores desejados

import requests #importa a biblioteca(sempre no topo)

##1- pedir ao usuário que insira a sigla da moeda
selecao_moeda = input("Escolha os pares das moedas desejadas separadas por um '-' e separados por vírgula sem espaço (ex: usd-brl,usd-jpy) : ")
print('\n', selecao_moeda.upper())

##2- armazenar url e concatenar com a entrada do usuário
url = (f'https://economia.awesomeapi.com.br/json/last/{selecao_moeda}')
pares = selecao_moeda.split(',')

##3- processar cada par (devido a limitação da API)
for par in pares:
  url = f'https://economia.awesomeapi.com.br/json/last/{par}'
  response = requests.get(url)

##4- se não encontrar, inverter a ordem do par (devido a limitação da API)
  if response.status_code == 404 and '-' in par:
    base, quote = par.split('-')
    par_invertido = f"{quote}-{base}"
    print('\n',f"tentando inverter para: {par_invertido}")
    url = f"https://economia.awesomeapi.com.br/json/last/{par_invertido}"
    response = requests.get(url)
    par = par_invertido
  
  ##5- convertendo requisição em JSON
  if response.status_code == 200:
    dados = response.json()
    print('\n', dados)
    print('\n', dados.keys()) ###utilizei  o \n para facilitar minha visualização
  else:
    print("erro na requisição", response.status_code)
  
##6- retornando valores em dicionário  
chave = list(dados.keys())[0]
nome_par = dados[chave]['name']
print(nome_par)

