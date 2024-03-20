# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float(input('Digite um número qualquer: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')
print(int(num))
print(num.__floor__())
