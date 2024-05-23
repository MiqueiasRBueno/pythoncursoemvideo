# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')), int(input('Digite mais outro número: ')))
print(f'Você digitou os valores: ', end='')
for n1 in num:
    print(n1, end=' ')
print(f'\nO valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('Não temos valore 3 em nossa tupla')
print(f'Os valores pares são', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')
