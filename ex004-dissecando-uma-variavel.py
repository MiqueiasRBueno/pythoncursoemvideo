# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre
# ele.

cor = dict(fim='\033[m', verm='\033[1;31m', az='\033[1;34m', amar='\033[1;33m', verd='\033[1;32m')
tipo = input(f'{cor['az']}Digite algo:{cor['fim']} ')
print(f'{cor['amar']}O tipo primitivo de valor é, {(type(tipo))}{cor['fim']}')
print(f'{cor['verd']}Só tem espaços? {tipo.isspace()}{cor['fim']}')
print(f'{cor['az']}É um número? {tipo.isnumeric()}{cor['fim']}')
print(f'{cor['verm']}É alfabético? {tipo.isalpha()}{cor['fim']}')
print(f'{cor['amar']}É alfanumérico? {tipo.isalnum()}{cor['fim']}')
print(f'{cor['az']}Está em maiúscula? {tipo.isupper()}{cor['fim']}')
print(f'{cor['verm']}Está em minúscula? {tipo.islower()}{cor['fim']}')
print(f'{cor['amar']}Está capitalizada? {tipo.istitle()}{cor['fim']}')
