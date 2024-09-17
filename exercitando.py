from time import sleep

ficha = []
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
print(f'{'N°':<4}{'NOME DO ALUNO':<10}{'MÉDIA':>8}')
print('-' * 25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{media:>11.1f}')
    print('-' * 25)
while True:
    aluno = int(input('Qual aluno deseja mostrar as notas? (999 interrompe): '))
    if aluno == 999:
        break
    if aluno <= len(ficha) -1:
        print(f'{'ALUNO':<10}{'NOTAS':>13}')
        print('-' * 25)
        print(f'{ficha[aluno][0]:<15}{ficha[aluno][1]}')
        print('-' * 25)
sleep(0.5)
print('Finalizando...')
