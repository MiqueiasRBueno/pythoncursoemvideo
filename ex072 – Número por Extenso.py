# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
        'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
        'DEZENOVE', 'VINTE')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20:
        print('Tente denovo! ', end=' ')
    else:
        if 0 > num:
            print('Tente denovo! ', end=' ')
        else:
            print(f'Você digitou o \033[1;33m{cont[num]}\033[m!')
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if parar == 'N':
        break
print('\033[31mPrograma finalizado com sucesso!\033[m')