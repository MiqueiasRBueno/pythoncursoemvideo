# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores: ', end=' ')
for n in numeros:
    print(f'\033[1;33m{n}\033[m', end=' ')
print(f'\nO maior valor foi \033[1;31m{max(numeros)}\033[m')
print(f'O menor valor foi \033[1;31m{min(numeros)}\033[m')
