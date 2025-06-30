# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    url = urllib.request.urlopen("https://greenvirtual.com.br/")
except urllib.error.URLError:
    print('O site Pudim não está acessível!')
else:
    print('O site Pudim está acessível!')
