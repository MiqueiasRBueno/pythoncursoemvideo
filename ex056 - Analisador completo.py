# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
maior_id = 0
novinha = 0
qtd = 0
for p in range(1, 5):
    nome = str(input(f'Digite o nome da {p}ª pessoa: ')).strip().title()
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))
    genero = str(input(f'Digite o gênero da {p}ª pessoa: ')).strip().upper()
    media += idade / 4  # Calcula a média de idade do grupo
    if p == 1:  # analisa o primeiro laço
        maior_id = idade
        novinha = idade
        nom_old = genero == 'MASCULINO'
        qtd += novinha < 20
    else:  # compara os laços seguintes
        if idade > maior_id:
            maior_id = idade
            nom_old = genero == 'MASCULINO'
            print(f'O nome do homem mais velho do grupo é {nom_old}')
        if idade < novinha:
            novinha = idade
print(f'A média de idade do grupo é de {media:.0f} anos')

print(f'A mulher mais nova tem {novinha} anos')
