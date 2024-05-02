# Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada.

from math import sqrt
while True:
    num = int(input('Digite um número: '))
    print(f'O dobro de \033[31m{num}\033[m é \033[32m{num * 2}\033[m')
    print(f'E o triplo de \033[31m{num}\033[m é {num * 3}')
    print(f'E a raiz quadrada de \033[31m{num}\033[m é \033[33m{sqrt(num):.2f}\033[m')
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if parar == 'N':
        break
print('\033[36mAnalise concluída!\033[m')
