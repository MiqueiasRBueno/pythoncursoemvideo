# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
mulheres = 0
maior = 0
old = ''
for p in range(1, 5):
    print(f'\033[1;32m------------------ {p}ª ------------------\033[m')
    nome = str(input(f'Digite o nome da {p}ª pessoa: ')).strip().title()
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))
    sexo = str(input(f'Digite o gênero [M / F] da {p}ª pessoa: ')).strip().upper()
    print(f'\033[1;32m----------------------------------------\033[m')
    if sexo == 'F':
        mulheres += idade < 20
    if p == 1 and sexo == 'M':
        maior = idade
        old = nome
    if idade > maior and sexo == 'M':
        maior = idade
        old = nome
    media += idade / 4
print(f'O homem mais velho do grupo se chama \033[1;32m{old}\033[m e tem \033[1;33m{maior}\033[m anos')
print(f'A média de idade do grupo é de \033[1;31m{media:.0f}\033[m anos.')
print(f'No grupo temos \033[1;36m{mulheres}\033[m mulher(es) menor(es) de \033[1;31m20\033[m anos.')
