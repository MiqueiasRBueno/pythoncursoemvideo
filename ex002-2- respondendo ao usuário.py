# Crie um script que leia o nome de uma pessoa e mostre uma mensagem de Boas-vindas segundo o valor digitado:

while True:
    nome = str(input('Digite seu nome: ')).strip().title()
    print(f'\033[32mOlá {nome}, é um prazer te conhecer!\033[m')
    segue = ' '
    while segue not in 'SN':
        segue = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if segue == 'N':
        break
