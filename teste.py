matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = maior_linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print(f'\033[1;32m-=\033[m' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print('\033[1;32m-=\033[m' * 30)
for coluna in range(0, 3):
    if coluna == 0:
        matriz[1][coluna] = maior_linha
    elif matriz[1][coluna] > maior_linha:
        maior_linha = matriz[1][coluna]
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna {soma_coluna}')
print(f'A soma dos valores pares digitados {soma_pares}')
print(f'O maior valor da segunda linha é {maior_linha}')