# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from time import sleep
num = int(input('Informe um número de 0 a 9999: '))
un = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print(f'Analisando o número {num}')
for c in range(0,3):
    print('Processando...')
    sleep(1)
print(f'Unidade: {un}\nDezena:  {dez}\nCentena: {cent}\nMilhar:  {mil}')
