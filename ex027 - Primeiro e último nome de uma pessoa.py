# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

nome = str(input('Qual é o seu nome completo? ')).strip().title()
spl_nome = nome.split()[0]
spl_sobre = nome.rsplit()[-1]
print(f'Seu nome completo é \033[1;33m{nome}\033[m')
print(f'Seu primeiro nome é \033[1;34m{spl_nome}\033[m')
print(f'Seu último nome é \033[1;36m{spl_sobre}\033[m')
