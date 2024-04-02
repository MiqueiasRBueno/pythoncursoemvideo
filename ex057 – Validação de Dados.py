# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [ F/M ]: ')).upper()  # Contém a condição a ser comparada
while sexo != 'F' and sexo != 'M':  # Compara se a condição é verdadeira ou falsa
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [F/M]: ')).upper()  # se condição for falsa essa
    # condição passa a ser verificada se verdadeira ou falsa.
if sexo == 'F':
    print(f'Sexo \033[1;35mFEMININO\033[m registrado com sucesso!')
elif sexo == 'M':
    print('Sexo \033[1;32mMASCULINO\033[m validado com sucesso!')
