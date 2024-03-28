# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = float(input('Digite um número qualquer: '))
if num % 2 == 0:
    print(f'O número \033[1;32m{num:.2f}\033[m é um número par!')
else:
    print(f'O número \033[1;32m{num:.2f}\033[m é um número impar!')
