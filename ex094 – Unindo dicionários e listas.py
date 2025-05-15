# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cad_pessoas_dicio = dict()
cad_pessoas_lista = list()
indices = media = soma = 0
while True:
    cad_pessoas_dicio.clear()
    cad_pessoas_dicio['Nome'] = str(input('Nome: ')).title().strip()
    while True:
        cad_pessoas_dicio['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if cad_pessoas_dicio['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite somente M ou F!')
    cad_pessoas_dicio['Idade'] = int(input('Idade: '))
    media += cad_pessoas_dicio['Idade']
    cad_pessoas_lista.append(cad_pessoas_dicio.copy())
    while True:
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if stop in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if stop == 'N':
        break
if len(cad_pessoas_lista) > 1:
    print(f'A) Foram cadastradas {len(cad_pessoas_lista)} pessoas')
else:
    print(f'A) Foi cadastrada {len(cad_pessoas_lista)} pessoa')
print(f'B) A média de idade entre as pessoas cadastradas é de {media / len(cad_pessoas_lista):5.2f} anos')
print(f'C) As mulheres cadastradas são: ', end=' ')
for p in cad_pessoas_lista:
    if p['Sexo'] == 'F':
        print(p['Nome'], end=' ')
print()
print(f'D) Pessoas cadastrada acima da média de idade:')
for p in cad_pessoas_lista:
    if p['Idade'] > media / len(cad_pessoas_lista):
        for k, v in p.items():
            print(f' {k} = {v}', end=' ')
        print()
