# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date
ano = date.today().year
jovens = 0
velhos = 0
for c in range(1, 8):
    num = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = ano - num
    jovens += idade <= 18
    velhos += idade > 18
print(f'Ao todo tivemos \033[1;31m{velhos}\033[m pessoas maiores de idade'
      f'\nE também tivemos \033[1;33m{jovens}\033[m pessoas menores de idade. ')
