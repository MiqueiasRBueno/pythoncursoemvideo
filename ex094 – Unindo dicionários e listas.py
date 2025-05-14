# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cad_pessoas_dicio = dict()
cad_pessoas_lista = list()
mulheres = list()
indices = media = soma = 0
while True:
    cad_pessoas_dicio.clear()
    cad_pessoas_dicio['Nome'] = str(input('Nome: ')).title().strip()
    sexo = ' '
    while sexo not in 'MF':
        cad_pessoas_dicio['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if cad_pessoas_dicio['Sexo'] in 'F':
            mulheres.append(cad_pessoas_dicio['Nome'])
        sexo = cad_pessoas_dicio['Sexo']
        if cad_pessoas_dicio['Sexo'] not in 'MF':
            print('ERRO! Por favor, digite somente M ou F!')
    if sexo == 'MF':
        break
    idade = int(input('Idade: '))
    cad_pessoas_dicio['Idade'] = idade
    media += idade / 2
    cad_pessoas_lista.append(cad_pessoas_dicio.copy())

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if stop not in 'SN':
            print('ERRO! Responda apenas S ou N.')
    if stop == 'N':
        break
if len(cad_pessoas_lista) > 1:
    print(f'A) Foram cadastradas {len(cad_pessoas_lista)} pessoas')
else:
    print(f'A) Foi cadastrada {len(cad_pessoas_lista)} pessoa')
print(f'B) A média de idade entre as pessoas cadastradas é de {media:.1f} anos')
if len(mulheres) > 0:
    if len(mulheres) > 1:
        print(f'C) As mulheres cadastradas são: ', end=' ')
    else:
        print(f'C) A mulher cadastrada é: ', end=' ')
    for m in mulheres:
        print(m, end=' ')
else:
    print('C) Não temos mulheres cadastradas!')
print()
for p in cad_pessoas_lista:
    if p['Idade'] >= media:
        print(' ')
        for k, v in p.itens():
            print(f'{k} = {v}:', end=' ')
        print()