# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 40)
print('{:^48}'.format('\033[31mBANCO PERDIDIMMM\033[m'))
print('=' * 40)
valor = int(input('Digite o valor que deseja sacar: R$ '))
total = valor
cedulas = 50
totalced = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totalced += 1
    else:
        if totalced > 0:
            print(f'Foram sacadas {totalced} cédula(s) de R$ {cedulas:.2f}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        elif cedulas == 2:
            cedulas = 1
        totalced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO PERDIDIMMM! Tenha um bom dia!')
