# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
pc = randint(0, 100)
print('VAMOS JOGAR PAR OU IMPAR?')
print(pc)
soma = 0
while True:
    num = int(input('Digite um valor: '))
    par_impar = str(input('Par ou Impar? [P/I] ')).upper().strip()
    par = (num + pc) % 2
    if par_impar == 'P' and par != 0:
        break
    if par_impar == 'I' and par == 0:
        break
    if par_impar == 'P' and par == 0:
        print(f'Você jogou {num} e o computador {pc}. Total de {num + pc} DEU PAR!')
        print('Você venceu!\nVamos jogar novamente...')
    elif par_impar == 'I' and par != 0:
        print(f'Você jogou {num} e o computador {pc}. Total de {num + pc} DEU IMPAR!')
        print('Você venceu!\nVamos jogar novamente...')
    soma += 1
print(f'Você ganhou {soma} veze(s)')
print('GAME OVER, você perdeu!')
