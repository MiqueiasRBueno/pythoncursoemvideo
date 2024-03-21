# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Digite o 1º aluno: ')).strip().title()
n2 = str(input('Digite o 2º aluno: ')).strip().title()
n3 = str(input('Digite o 3º aluno: ')).strip().title()
n4 = str(input('Digite o 4º aluno: ')).strip().title()
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem para apresentarem seus trabalhos é :\n{}'.format(lista))
