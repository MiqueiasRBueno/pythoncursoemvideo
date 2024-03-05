# Faça um programa que leia um número inteiro e mostre o seu sucessor e antecessor.

num = int(input('Digite um número inteiro qualquer: '))
ant = (num - 1)
suc = (num + 1)
print(f'O número \033[1;32m{ant:.0f}\033[m é o antecessor de \033[1;33m{num:.0f}\033[m que tem seu sucessor'
      f' o número \033[1;31m{suc:.0f}\033[m')
