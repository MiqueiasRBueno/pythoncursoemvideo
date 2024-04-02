# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [ F/M ]: ')).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [F/M]: ')).upper()
print(f'Sexo {sexo} registrado com sucesso!')
