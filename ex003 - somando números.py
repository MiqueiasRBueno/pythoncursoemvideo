# Crie um programa que leia dois números e mostre a soma entre eles.

while True:
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite mais um valor: '))
    print(f'\033[31mA soma entre {num1} e {num2} vale {num1 + num2}\033[m')
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if parar == 'N':
        break
