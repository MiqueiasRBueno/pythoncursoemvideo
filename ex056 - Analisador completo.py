# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
mulheres = 0
maior = 0
old = ''
for p in range(1, 5):
    nome = str(input(f'Digite o nome da {p}ª pessoa: ')).strip().title()
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))
    print('''Gênero
    [ M ] (masculino) 
    [ F ] (feminino)''')
    sexo = str(input(f'Digite o gênero da {p}ª pessoa: ')).strip().upper()
    if sexo == 'F':
        mulheres += idade < 20
    if p == 1 and sexo == 'M':
        maior = idade
        old = nome
    if idade > maior and sexo == 'M':
        maior = idade
        old = nome
    media += idade / 4
print(f'O homem mais velho do grupo se chama {old} e tem {maior} anos')
print(f'A média de idade do grupo é de {media:.0f}')
print(f'No grupo temos {mulheres} mulher(es) menor(es) de 20 anos.')
