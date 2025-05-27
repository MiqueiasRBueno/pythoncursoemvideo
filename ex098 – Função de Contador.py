# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(i, fim, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('\033[1;31m=\033[m' * 40)
    print (f'Contagem de {i} até {fim}, de {p} em {p}')

    if i < fim:
        cont = i
        while cont <= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont += p
        print('Fim!')
    if i > fim:
        cont = i
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= p
        print('Fim!')


# Programa Principal:
contador(1, 10, 1)
contador(10, 0, 2)
print('\033[1;31m=\033[m' * 40)
print('Agora é sua vez de escolher sua contagem:')
inicio = int(input('Início: '))
fim1 = int(input('Fim: '))
pas = int(input('Passo: '))
contador(inicio, fim1, pas)