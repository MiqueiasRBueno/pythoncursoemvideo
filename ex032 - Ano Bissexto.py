# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
print('\033[1;32m', '=' * 4, '\033[m\033[1;33mANALISADOR DE ANO BISSEXTO!\033[m', '\033[1;32m', '=' * 4, '\033[m')
print('Digite 0 para o ano atual!')
ano = int(input('Que ano quer analisar? '))
atual = date.today().year
if ano % 4 == 0 and ano % 400 == 0:
    if ano == 0 and ano % 400 == 0:
        ano = atual % 4
        print(f'O ano de {atual}, é um ano \033[1;32mBISSEXTO\033[m!')
    else:
        print(f'O ano de {ano}, é um ano \033[1;34mBISSEXTO\033[m!')
else:
    print(f'O ano de {ano} não é um ano \033[32;1mBISSEXTO\033[m!')
