# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

no_1 = float(input('Qual o valor da primeira nota de seu aluno? '))
no_2 = float(input('Qual o valor da segunda nota de seu aluno? '))
s = (no_1 + no_2)
med = s/2
print(f'A soma da primeira nota \033[1;33m{no_1:.2f}\033[m e a segunda \033[33;1m{no_2:.2f}\033[m '
      f'de seu aluno é \033[33;1m{s:.2f}\033[m')
if med >= 7:
    print(f'A média entre elas é \033[1;34m{med:.2f}\033[m')
    print('\033[1;42;30m Meus parabéns, você foi aprovado! \033[m')
else:
    print(f'A média entre elas é \033[1;31m{med:.2f}\033[m')
    print('\033[40;7;1m Que pena, você precisa estudar mais! \033[m')
