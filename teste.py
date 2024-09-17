imp_par = [[], []]
for n in range(0, 7):
    num = int(input(f'Digite o {n + 1}° valor: '))
    if num % 2 == 0:
        imp_par[0].append(num)
    else:
        imp_par[1].append(num)
print(f'Os números pares cadastrados são: {imp_par[0]}')
print(f'E os números impares cadastrados são: {imp_par[1]}')
print('-=' * 30)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = ter_coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valora para [{l}:{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-=' * 30)
print(f'A soma dos números pares: {soma_pares}')
for l in range(0, 3):
    ter_coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna: {ter_coluna}')
for c in range(0, 3):
    if matriz[1][c] == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número encontrado na segunda linha é : {maior}')
print('-=' * 30)

