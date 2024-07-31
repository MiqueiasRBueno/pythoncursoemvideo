# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro_temp = []
cadastro_princ = []
maior = menor = 0
while True:
    cadastro_temp.append(str(input('Cadastre o nome: ')).title().strip())
    cadastro_temp.append(float(input('Cadastre o peso: ')))
    if len(cadastro_princ) == 0:
        maior = menor = cadastro_temp[1]
    else:
        if cadastro_temp[1] > maior:
            maior = cadastro_temp[1]
        if cadastro_temp[1] < menor:
            menor = cadastro_temp[1]
    cadastro_princ.append(cadastro_temp[:])
    cadastro_temp.clear()
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if parar == 'N':
        break
print(f'O total cadastrados é de {len(cadastro_princ)} pessoas.')
print(f'O maior peso cadastrado é de {maior}kg. Peso de ', end=' ')
for p in cadastro_princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso é de {menor}kg. Peso de ', end=' ')
for p in cadastro_princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
