# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando o flag).
num = ''
som2 = 0
soma = 0
total = 0
while num != 999:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    soma += num
    total = soma - 999
    som2 += 1
print(f'Você digitou {som2 - 1} números, e o resultado da soma entre eles é {total}. ')
