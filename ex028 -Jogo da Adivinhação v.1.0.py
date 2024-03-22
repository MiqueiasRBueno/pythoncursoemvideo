# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint
print('Tente adivinhar o número que o computador pensou!')
sorteio = randint(0, 5)
num = int(input('Digite um número entre 0 e 5: '))
if num == sorteio:
    print('Você escolheu o {} e o computador {}!'.format(num, sorteio))
    print('Você ACERTOU!')
else:
    print('Você ERROU, tente de novo!')
