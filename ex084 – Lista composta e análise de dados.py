# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas_cadastradas = list()
pesadas = []
leves = []
total_pessoas = 0
while True:
    pessoas_cadastradas.append(str(input('Nome: ')))
    pessoas_cadastradas.append(int(input('Peso: ')))
    total_pessoas += 1
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Quer continuar? [S/N]> ')).upper().strip()[0]
    if parar == 'N':
        break
print(f'O total de pessoas cadastradas foi de {total_pessoas} pessoas')
print(f'O maior peso foi de  . Peso de ')
print(f'O menor peso cadastrado foi de . Peso de ')
print(pessoas_cadastradas)
