# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

sn = ''
num = soma = cont = maior = menor = 0
while sn != 'N':
    num = int(input('Digite um número: '))
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += num
    cont += 1
    if maior == 0:
        maior += num
        menor += num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {cont} números e a média entre eles é {soma / cont:.2f}'
      f'\nE o maior valor foi {maior} e o menor foi {menor}')
