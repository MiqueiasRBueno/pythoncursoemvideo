# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    print('\033[1;31m=\033[m' * 45)
    print('Analisando valores passados.', end='')
    for p in range(0, 5):
        sleep(0.5)
        print('.', end='')
    print()
    sleep(0.5)
    tot = 0
    if len(num) <= 0:
        print(f'''_Foi digitado {tot} valores!
_O maior valor digitado é 0.''')
    else:
        for c in num:
            print(c, end=' ')
            sleep(0.5)
            tot += 1
        print(f'''_Foi digitado {tot} valores.
_O maior valor digitado é {max(num)}.''')


maior(1,4,7,8,0,3,2,90)
maior(2,4,6,8,0,7,5,3,755)
maior()
