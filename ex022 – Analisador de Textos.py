# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras no total (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
nometam = len(nome) - nome.count(' ')
print('Nome em:'
      f'\nMaiúsculas: \033[1;31m{nome.upper()}\033[m'
      f'\nMinúsculas: \033[1;32m{nome.lower()}\033[m'
      f'\nTotal de letras, sem espaços: \033[1;33m{nometam}\033[m'
      f'\nTotal de letras no primeiro nome: \033[34;1m{len(nome.split()[0])}\033[m')
