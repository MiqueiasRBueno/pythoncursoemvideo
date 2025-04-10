# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('\033[1;31m-=-\033[m' * 30)
print(' ' * 25, 'SEQUÊNCIA DE FIBONACCI', )
print('\033[1;31m-=-\033[m' * 30)
n = int(input("Quantos termos deseja mostrar: "))
t1 = 0  # valor do primeiro termo
t2 = 1  # valor do segundo termo
count = 3  # contará a partir do 3º termo
print(t1, '\033[1;31m¬\033[m', t2, end=' \033[1;31m¬\033[m ')
while count <= n:  # enquanto count menor ou igual a 'n', a repetição será executada
    count += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end='\033[1;31m ¬\033[m ')
print('\033[1;32mFIM\033[m')
