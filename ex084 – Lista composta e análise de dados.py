# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cad_pessoas_temp = []
cad_pessoas_princ = []
maior = menor = 0
while True:
    cad_pessoas_temp.append(str(input('Cadastre o nome: ')).title().upper().strip())
    cad_pessoas_temp.append(float(input('Cadastre o peso: ')))
    if len(cad_pessoas_princ) == 1:
        maior = menor = cad_pessoas_temp[1]
    else:
        if cad_pessoas_temp[1] > maior:
            maior = cad_pessoas_temp[1]
        if cad_pessoas_temp[1] < menor:
            menor = cad_pessoas_temp[1]
    cad_pessoas_princ.append(cad_pessoas_temp[:])
    cad_pessoas_temp.clear()
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if parar == 'N':
        break
print(f'O total de pessoas cadastradas é de {len(cad_pessoas_princ)} pessoas.')
print(f'O maior peso é de {maior:.2f}kg. O peso de: ', end=' ')
for p in cad_pessoas_princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso cadastrado é de {menor:.2f}kg. O peso de: ', end=' ')
for p in cad_pessoas_princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
