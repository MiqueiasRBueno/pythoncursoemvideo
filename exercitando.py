# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiores = homens = mulheres = menores = 0
while True:
    print('CADASTRAMENTO DE PESSOAS')
    ida = int(input('Idade: '))
    sex = str(input('Sexo: [F/M] ')).upper().strip()[0]
    ct = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    maiores += ida >= 18
    homens += sex.count('M')
    mulheres += sex.count('F')
    menores += ida <= 20
    if ct == 'N':
        break
print(f'acabou! {maiores}, {homens}, {mulheres}, {menores}')
