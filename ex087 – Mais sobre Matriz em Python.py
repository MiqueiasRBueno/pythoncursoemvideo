# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('\033[1;32m-=\033[m' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print('\033[1;32m-=\033[m' * 30)
print(f'A soma dos valores pares são: {soma_pares}')
soma = (matriz[0][2] + matriz[1][2] + matriz[2][2])
print(f'A soma dos valores da terceira coluna são: {soma}')
print(f'O maior valora da segunda linha é {max(matriz[1])}')
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f'Soma coluna Guanabara: {soma_coluna}')
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior do Guanabara : {maior}')