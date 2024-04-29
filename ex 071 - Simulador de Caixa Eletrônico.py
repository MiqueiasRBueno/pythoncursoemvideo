# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 40, '\n{:^40}'.format('BANCO PERDIDIMMM'))
print('=' * 40)
while True:
    num = int(input('Qual valor quer sacar? '))
    cinq = num // 50
    vinte = num % 50 // 20
    dez = num % 50 % 20 // 10
    cinco = num % 50 % 10 // 5
    um = num % 50 % 5 // 1
    if cinq > 0:
        print(f'Foram sacadas {cinq:.0f} notas de R$ 50,00')
    if vinte > 0:
        print(f'Foran sacadas {vinte:.0f} notas de R$ 20,00')
    if dez:
        print(f'Foram sacadas {dez:.0f} notas de R$ 10,00')
    if cinco:
        print(f'Foram sacadas {cinco:.0f} notas de R$ 5,00')
    if um > 0:
        print(f'Foram sacadas {um:.0f} notas de R$ 1,00')
    if num == num:
        break
print('=' * 40)
print('Volte sempre ao BANCO PERDIDIMMM! Tenha um bom dia!')
