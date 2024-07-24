# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas_cadastradas = list()
pessoas_mais = list()
pessoas_menos = list()
total_pessoas = maior = menor = 0
while True:
    pessoas_cadastradas.append(str(input('Cadastre o nome da pessoa: ')))
    pessoas_cadastradas.append(int(input('Cadastre o peso da pessoa: ')))
    total_pessoas += 1
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Quer continuar? [S/N]> ')).upper().strip()[0]
    if parar == 'N':
        break
print(f'O total de pessoas cadastradas foi de {total_pessoas} pessoas')
print(pessoas_cadastradas)
