# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

ficha = list()
while True:
    nome = str(input('Nome do aluno: ')).title().strip()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if parar == 'N':
        break
print('-=' * 30)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i + 1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    aluno = mostrar - 1
    if aluno == 998:
        print('Finalizando...')
        break
    if aluno <= len(ficha) - 1:
        print(f'Notas de {ficha[aluno][0]} são {ficha[aluno][1]}')