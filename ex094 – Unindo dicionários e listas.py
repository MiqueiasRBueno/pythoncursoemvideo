# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cad_pessoas_dicio = dict()
cad_pessoas_lista = list()
while True:
    cad_pessoas_dicio['Nome'] = str(input('Nome: ')).title().strip()
    cad_pessoas_dicio['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    cad_pessoas_dicio['Idade'] = int(input('Idade: '))
    cad_pessoas_lista.append(cad_pessoas_dicio.copy())
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if stop == 'N':
        break
if len(cad_pessoas_lista) > 1:
    print(f'Foram cadastradas {len(cad_pessoas_lista)} pessoas')
else:
    print(f'Foi cadastrada {len(cad_pessoas_lista)} pessoa')
print(cad_pessoas_dicio)
print(cad_pessoas_lista)