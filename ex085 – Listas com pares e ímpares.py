# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

num_temp = []
num_cadastrados = []
num_pares = []
num_impares = []
pos = 0
for num in range(0, 7):
    pos += 1
    num_temp.append(int(input(f'Digite o {pos}º número: ')))
    num_cadastrados.append(num_temp[:])
    for valor in num_temp:
        if valor % 2 == 0:
            num_pares.append(valor)
        else:
            num_impares.append(valor)
    num_temp.clear()
print(f'Lista de números cadastrados: {num_cadastrados}')
print(f'Os números pares cadastrados foram: {sorted(num_pares)}')
print(f'Os números ímpares cadastrados foram: {sorted(num_impares)}')
