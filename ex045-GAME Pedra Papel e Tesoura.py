# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep
print('\033[1;36m-)' * 5, '\033[m\033[1;32mPEDRA, PAPEL E TESOURA!\033[m', '\033[1;36m(-' * 5, '\033[m')
print('\033[1;33m= ' * 23, '\033[m', '\033[1m')
print('\033[1;33m= ' * 23, '\033[m', '\033[1m')
print('''SUAS OPÇÕES:
[ 1 ] PEDRA
[ 2 ] TESOURA
[ 3 ] PAPEL''')
opcao = int(input('Qual é a sua jogada? '))
print('\033[1;33m= ' * 23, '\033[m')
print('\033[1;33m= ' * 23, '\033[m')
sleep(0.85)
print('JO')
sleep(0.85)
print('KEM')
sleep(0.85)
print('PÔ !!!')
sleep(1)
list_opcao = ('PEDRA', 'TESOURA', 'PAPEL')
selecao = random.choice(list_opcao)
print('\033[33;1m= ' * 23, '\033[m')
print('\033[33;1m= ' * 23, '\033[m')
print(f'O computador escolheu {selecao}')
if opcao == 1:
    print('Você escolheu PEDRA')
    if selecao == 'PEDRA':
        print('EMPATE!')
    elif selecao == 'TESOURA':
        print('Jogador GANHOU!')
    elif selecao == 'PAPEL':
        print('Computador GANHOU!')
elif opcao == 2:
    print('Você escolheu TESOURA')
    if selecao == 'TESOURA':
        print('EMPATE!')
    elif selecao == 'PAPEL':
        print('Jogador GANHOU!')
    elif selecao == 'PEDRA':
        print('Computador GANHOU!')
elif opcao == 3:
    print('Você escolheu PAPEL')
    if selecao == 'PAPEL':
        print('EMPATE!')
    elif selecao == 'TESOURA':
        print('Computador GANHOU!')
    elif selecao == 'PEDRA':
        print('Jogador GANHOU!')
else:
    print('Alternativa incorreta, TENTE DE NOVO!')
print('\033[1;33m= ' * 23, '\033[m')
print('\033[1;33m= ' * 23, '\033[m')
