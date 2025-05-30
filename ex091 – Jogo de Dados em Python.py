# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from operator import itemgetter
from random import randint
from time import sleep

print(f'\033[1;31m{'=' * 30}\033[m')
sleep(1)
print(f'{'JOGO DE DADOS':-^30}')
sleep(1)
print(f'\033[1;31m{'=' * 30}\033[m')
jogos = {'Jogador 01': randint(1, 6), 'Jogador 02': randint(1, 6),
         'Jogador 03': randint(1, 6), 'Jogador 04': randint(1, 6)}
ranking = []
sleep(1)
print(f'\033[1;32m{'VALORES SORTEADOS':-^30}\033[m\n')
for k, v in jogos.items():
    sleep(1)
    print(f'{f'{k} tirou {v}':_^30}')
sleep(1)
print(f'\033[1;31m{'=' * 30}\033[m')
sleep(1)
print(f'\033[1;33m{'RANKING DE JOGADORES':-^30}\033[m\n')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{f'{i + 1}º lugar: {v[0]} com {v[1]}':_^30}')
print(f'\033[1;31m{'=' * 30}\033[m')
