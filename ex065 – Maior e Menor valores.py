# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

sn = ''
num = 0
soma = 0
cont = 0
while sn != 'N':
    num = int(input('Digite um número: '))
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
    soma += num
    cont += 1
print(soma / cont)