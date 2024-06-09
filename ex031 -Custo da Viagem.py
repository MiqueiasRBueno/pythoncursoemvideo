# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50
# por km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância à percorrer um sua viagem: '))
if distancia <= 200:
    preco = distancia * 0.45
    print(f'O valor a ser pago por sua viagem é de R$\033[1;33m{preco:.2f}\033[m')
else:
    preco = distancia * 0.5
    print(f'O valor a ser pago por sua viagem é de R$\033[33;1m{preco:.2f}\033[m')
