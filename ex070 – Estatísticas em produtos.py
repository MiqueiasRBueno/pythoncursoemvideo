# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-' * 40)
print('{: ^40}'.format('PERDIDIMMM SHOP'))
print('-' * 40)
total = maior = menor = cont = 0
barato = ''
while True:
    prod = str(input('Nome do produto: ')).strip()
    preco = float(input('PREÇO: R$ '))
    conti = ' '
    total += preco
    cont += 1
    if preco > 1000:
        maior += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    while conti not in 'NS':
        conti = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    if conti == 'N':
        break
print('-' * 40)
print('{: ^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de  R$ \033[1;31m{total:.2f}\033[m.')
if maior > 1:
    print(f'Temos {maior} produtos custando mais de R$ \033[1;31m1000,00\033[m.')
else:
    print(f'Temos {maior} produto custando mais de R$ \033[1;31m1000.00\033[m.')
print(f'O produto mais barato foi o(a){barato}.')
