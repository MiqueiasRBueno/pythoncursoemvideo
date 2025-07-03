# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests

try:
    resposta = requests.get('http://www.pudim.com.br')
    resposta.raise_for_status()
    print('Site Pudim está acessível!')
except requests.exceptions.RequestException:
    print('O site Pudim não está acessível!')
