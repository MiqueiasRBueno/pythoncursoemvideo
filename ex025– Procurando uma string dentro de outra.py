# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual é o seu nome completo? ')).strip()
up = nome.upper()
silva = 'SILVA' in up
print('Seu nome tem Silva? {}'.format(silva))
