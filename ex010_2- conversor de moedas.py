# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

while True:
    carteira = float(input('Quantos reais você possui em sua carteira? R$'))
    dolar = float(input('Qual a cotação do dolar hoje? US$'))
    euro = float(input('Qual a cotação deo euro hoje? €'))
    convdl = carteira / dolar
    conveu = carteira / euro
    print(f' O montante de R$\033[1;32m{carteira:.2f}\033[m que você possui em sua carteira equivale a:'
          f'\n Dolar US$\033[1;31m{convdl:.2f}\033[m\n Euros €\033[1;31m{conveu:.2f}\033[m')
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if parar == 'N':
        break
print('Conversão finalizada com sucesso!')
