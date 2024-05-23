# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')), int(input('Digite mais outro número: ')))
print(f'Você digitou os valores: ', end='')
for n1 in num:
    print(f'\033[31m{n1}\033[m', end=' ')
print(f'\nO valor \033[33;1m9\033[m apareceu \033[31m{num.count(9)}\033[m vezes')
if 3 in num:
    print(f'O primeiro valor \033[1;33m3\033[m apareceu na \033[33;1m{num.index(3) + 1}ª\033[m posição')
else:
    print('Não temos valore \033[1;33m3\033[m em nossa tupla')
print(f'Os valores pares são', end=' ')
for n in num:
    if n % 2 == 0:
        print(f'\033[31m{n}\033[m', end=', ')
