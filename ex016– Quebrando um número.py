# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float(input('Digite um número qualquer: '))
print(f'O valor digitado foi \033[1;32m{num}\033[m e a sua porção inteira é \033[1;32m{trunc(num)}')
print(int(num))
print(num.__floor__())
