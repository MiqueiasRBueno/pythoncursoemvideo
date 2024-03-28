#  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num = float(input('Digite um número qualquer: '))
num2 = float(input('Digite um segundo número qualquer: '))
num3 = float(input('Digite um terceiro número qualquer: '))
if num > num2 and num > num3:
    print(f'O maior número entre {num:.2f}, {num2:.2f} e {num3:.2f} é o número \033[1;32m{num:.2f}\033[m')
    if num2 > num3:
        print(f'E o menor número é o \033[1;31m{num3:.2f}\033[m')
    elif num3 > num2:
        print(f'E o menor número é o \033[1;31m{num2:.2f}\033[m')
elif num2 > num3 and num2 > num:
    print(f'O maior número entre {num:.2f}, {num2:.2f} e {num3:.2f} é o número \033[1;32m{num2:.2f}\033[m')
    if num3 > num:
        print(f'E o menor número é o \033[1;31m{num:.2f}\033[m')
    elif num > num3:
        print(f'E o menor número é o \033[1;31m{num3:.2f}\033[m')
else:
    print(f'O maior número entre {num:.2f}, {num2:.2f} e {num3:.2f} é o número \033[1;32m{num3:.2f}\033[m')
    if num > num2:
        print(f'E o menor número é o \033[1;31m{num2:.2f}\033[m')
    else:
        print(f'E o menor número é o \033[1;31m{num:.2f}\033[m')
