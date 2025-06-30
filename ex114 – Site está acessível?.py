# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests

url = "http://www.pudim.com.br"
try:
    resp = requests.get(url)
    resp.raise_for_status()
    print(f'O site {url} está acessível!')
except requests.exceptions.RequestException:
    print(f'O site {url} não está acessível!')
