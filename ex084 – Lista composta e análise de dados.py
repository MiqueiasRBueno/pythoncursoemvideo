# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Cadastre um nome: ')).title().strip())
    temp.append(float(input('Cadastre o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if (temp[1]) > maior:
            maior = temp[1]
        if (temp[1]) < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    parar = ' '
    while parar not in 'SN':
        parar = (str(input('Deseja continuar? [S/N] '))).strip().upper()[0]
    if parar == 'N':
        break
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso cadastrado foi {maior:.2f}\033[31;1mkg\033[m. Peso de : ', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menor:.2f}\033[32;1mkg\033[m.', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
