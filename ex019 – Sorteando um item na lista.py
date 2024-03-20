# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
# o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
n1 = str(input('Digite o 1º aluno: ')).strip().title()
n2 = str(input('Digite o 2º aluno: ')).strip().title()
n3 = str(input('Digite o 3º aluno: ')).strip().title()
n4 = str(input('Digite o 4º aluno: ')).strip().title()
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(escolhido)
