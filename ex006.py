# Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada.

from math import sqrt
num = float(input('Digite um número qualquer: '))
dbr = num * 2
trp = num * 3
rqd = sqrt(num)
print(f'O dobro, triplo e raiz quadrada de \033[1;4;34m{num:.2f}\033[m é:\nDobro \033[1;4;32m{dbr:.2f}\033[m'
      f'\nTriplo \033[1;4;35m{trp:.2f}\033[m\nRaiz Quadrada \033[36;1;4m{rqd:.2f}\033[m')
