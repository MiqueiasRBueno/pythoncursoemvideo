# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
from time import sleep
num = int(input('Digite um número para calcular seu fatorial: '))
ft = num
mult = 1
sleep(0.5)
print(f'Calculando', end='')
for c in range(0, 6):
    sleep(1)
    print('.', end='')
print(f' {num}! = {num}', end=' ')
while ft != 1:
    ft -= 1
    mult *= ft + 1
    if ft > 0:
        print('X', end=' ')
    else:
        print('=', end=' ')
    print(ft, end=' ')

print(f'= {mult}')
