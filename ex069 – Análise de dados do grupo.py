# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiores = mulheres = 0
homens = 0
while True:
    print('-' * 40)
    print('CADASTRE UM PESSOA')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    conti = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    maiores += idade >= 18
    homens += sexo == 'M'
    if conti == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Temos {homens} homem(ns) cadastrados')
print('A quantidade de mulheres menores de 20 anos:')
