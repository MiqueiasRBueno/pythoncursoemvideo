# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
num = int(input('Tente adivinhar o número que o computador pensou entre 0 e 10: '))
sorteio = randint(0, 10)
vezes = 0
while num != sorteio:
    vezes += 1
    if num < sorteio:
        num = int(input('Você errou, tente novamente o número é >: '))
    if num > sorteio:
        num = int(input('Você errou, tente novamente o número é <:'))
print(f'Você escolheu o número \033[1;32m{num}\033[m e o computador também escolheu o \033[1;32m{sorteio}\033[m'
      f'\n\033[1;31mPARABÉNS\033[m você acertou com \033[1;33m{vezes + 1}\033[m tentativas!')
