# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = list()

# Função para sortear 5 números aleatórios:
def sorteia(lista):
    print(f'''\033[1;32m{'-' * 53}\033[m
Sorteando os 5 valores :''', end='')
    for point in range(0,3):
        print('.', end='')
        sleep(0.3)
    for sort in range(0, 5):
        values = randint(1, 10)
        lista.append(values)
    for value in lista:
        print(value, end=' ')
        sleep(0.3)
    print('PRONTO!')

# Função para somar números pares em uma lista:
def somapar(lista):
    print(f'Com a soma dos valores pares {lista}, temos', end=' ')
    soma = 0
    for value in lista:
        if value % 2 == 0:
            soma += value
    print(soma)


# Programa Principal:
sorteia(numeros)
somapar(numeros)
