# Faça um programa que leia um número inteiro e mostre o seu sucessor e antecessor.

while True:
    num = int(input('Digite um número: '))
    print(f'O número \033[31m{num - 1}\033[m é antecessor de '
          f'\033[31m{num}\033[m que tem seu sucessor o número \033[31m{num + 1}\033[m')
    parar = ' '
    while parar not in 'SN':
        parar = str(input('\033[36mQuer continuar analisando? [S/N]\033[m ')).upper().strip()[0]
    if parar == 'N':
        break
print('\033[34mAnálise concluída com sucesso!\033[m')
