# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from time import sleep
num = int(input('Digite um número para calcular seu fatorial: '))
ft = num
c = 0
mult = 1
sleep(0.5)
print('Calculando', end=' ')
for cal in range(1, 4):
    sleep(1.2)
    print('.', end=' ')
sleep(0.5)
print(num, '! =', num, end=' ')
for c in range(1, num):
    ft -= 1
    mult *= ft + 1
    sleep(0.5)
    print('x' if ft > 0 else '=', end=' ')
    print(ft, end=' ')
print('=', mult, end=' ')
