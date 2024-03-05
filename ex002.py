# Crie um script que leia o nome de uma pessoa e mostre uma mensagem de Boas-vindas segundo o valor digitado:

cor = dict(fim='\033[m', az='\033[1;34m')
nome = str(input('Qual seu nome? ')).strip().title()
print(f'Olá {cor['az']}{nome}{cor['fim']}!\nPrazer em te conhecer!')
