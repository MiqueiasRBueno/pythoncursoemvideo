# Crie um programa que leia dois números e mostre a soma entre eles.

cor = dict(fim='\033[m', verm='\033[1;31m', verd='\033[1;32m', amar='\033[1;33m', az='\033[1;34m')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = (n1 + n2)
print(f'A soma entre {cor['amar']}{n1}{cor['fim']} e {cor['amar']}{n2}{cor['fim']} vale {cor['az']}{s}{cor['fim']}!')
