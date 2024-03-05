# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.

num = int(input('Digite um número qualquer: '))
print('Base para conversão\n- 1 para binário\n- 2 para octal\n- 3 para hexadecimal')
conv = input('Escolha a base de conversão: ')
if conv == '1':
    print(f'O número {num} convertido em binário é {bin(num)[2:]}')
elif conv == '2':
    print(f'O número {num} convertido em octal é {oct(num)[2:]}')
elif conv == '3':
    print(f'O número {num} convertido em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente!')
