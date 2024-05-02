# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
notas = []
num = soma = 0
while True:
    num += 1
    nota = float(input(f'Digite a {num}ª nota do aluno: '))
    soma += nota
    notas.append(nota)
    if num == 2:
        break
print(f'A 1ª nota do aluno é \033[31m{notas[0]}\033[m\na 2ª nota do aluno é \033[31m{notas[1]}\033[m\n'
      f'E a média do aluno é de \033[34m{soma / 2:.2f}\033[m')
