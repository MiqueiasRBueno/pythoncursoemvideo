# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

num_cadastrados = [[], []]
valores = 0
for c in range(1, 8):
    valores = int(input(f'Digite o {c}° valor: '))
    if valores % 2 == 0:
        num_cadastrados[0].append(valores)
    else:
        num_cadastrados[1].append(valores)
print('\033[31m-=\033[m' * 30)
print(f'Valores pares cadastrados: {sorted(num_cadastrados[0])}')
print(f'Valores impares cadastrados: {sorted(num_cadastrados[1])}')
