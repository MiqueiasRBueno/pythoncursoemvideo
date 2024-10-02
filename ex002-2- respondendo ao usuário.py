# Crie um script que leia o nome de uma pessoa e mostre uma mensagem de Boas-vindas segundo o valor digitado:

nome = str(input('Digite seu nome: ')).strip().title()
print(f'\033[32mOlá {nome}, é um prazer te conhecer!\033[m')
