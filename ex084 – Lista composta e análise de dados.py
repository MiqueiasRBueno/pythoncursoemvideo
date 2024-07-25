# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro_temp = []
cadastro_princ = []
peso_maior = peso_menor = 0
while True:
    cadastro_temp.append(str(input('Cadastre um nome: ')))
    cadastro_temp.append(float(input('Cadastre o peso:')))
    if len(cadastro_princ) == 0:
        peso_maior = peso_menor = cadastro_temp[1]
    else:
        if cadastro_temp[1] > peso_maior:
            peso_maior = cadastro_temp[1]
        if cadastro_temp[1] < peso_menor:
            peso_menor = cadastro_temp[1]
    cadastro_princ.append(cadastro_temp[:])
    cadastro_temp.clear()
    parar = (str(input('Quer continuar? [S/N] ')))
    if parar in 'Nn':
        break
print(f'Foram cadastradas o total de {len(cadastro_princ)} pessoas.')
print(f'O maior peso cadastrado foi {peso_maior}kg. O peso de ', end=' ')
for p in cadastro_princ:
    if p[1] == peso_maior:
        print([p[0]], end=' ')
print()
print(f'O menor peso cadastrado foi {peso_menor}kg. O peso de ', end=' ')
for p in cadastro_princ:
    if p[1] == peso_menor:
        print([p[0]], end=' ')
