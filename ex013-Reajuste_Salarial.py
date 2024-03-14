# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

cor = dict(fim='\033[m', branco='\033[1;30m', verm='\033[1;31m', verd='\033[1;32m', amar='\033[1;33m',
           azul='\033[1;34m', roxo='\033[1;35m', cyan='\033[1;36m', inver='\033[1;37m')
salario_min = float(input('Digite o valor do sálario mínimo atual: R$ '))
salario = float(input('Digite o valor do sálario de seu funcionário: R$ '))
salario_base = salario // salario_min
if salario_base < 2:
    salario_aum = salario + (salario * 0.15)
    print(f'O funcionário recebe atualmente R$ {cor['amar']}{salario:.2f}{cor['fim']}'
          f'\nCom o aumento de 15% passará para R$ {cor['verd']}{salario_aum:.2f}{cor['fim']}')
elif salario_base < 3:
    salario_aum = salario + (salario * 0.08)
    print(f'O funcionário recebe atualmente R$ {cor['amar']}{salario:.2f}{cor['fim']}'
          f'\nCom o aumento de 8% passará para R$ {cor['verd']}{salario_aum:.2f}{cor['fim']}')
else:
    salario_aum = salario + (salario * 0.04)
    print(f'O funcionário recebe atualmente R$ {cor['amar']}{salario:.2f}{cor['fim']}'
          f'\nCom o aumento de 4% passará para R$ {cor['verd']}{salario_aum:.2f}{cor['fim']}')
