# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []
jogos = []
print('\033[1;32m-=\033[m' * 30)
print(' ' * 20, f'\033[1;33mJOGOS DA MEGA SENA\033[m')
print('\033[1;32m-=\033[m' * 30)
qtd = int(input('Quantos jogos deseja sortear? '))
total = 1
while total <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(' ' * 20, f'\033[1;33mSORTEANDO {qtd} JOGOS!\033[m')
print('\033[1;32m-=\033[m' * 30)
for i, l in enumerate(jogos):
    sleep(0.85)
    print(f'Jogo nº{i + 1}: {l}')
print('\033[1;32m-=\033[m' * 30)