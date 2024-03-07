# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme
# a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

not1 = float(input('Qual a primeira nota de seu aluno? '))
not2 = float(input('Qual é a segunda nota de seu aluno? '))
media = (not1 + not2) / 2
if media < 5:
    print(f'Que pena, sua média é de \033[1;31m{media:.1f}\033[m. \nAbaixo de \033[1;33m5.0\033[m'
          f', nota mínima para "\033[1;33mRECUPERAÇÃO\033[m".\nVocê foi "\033[1;31mREPROVADO\033[m"!')
elif media > 6.9:
    print(f'Meus parabéns! Sua média é de \033[1;34m{media}\033[m\nVocê foi "\033[1;34mAPROVADO\033[m"!')
else:
    print(f'Que pena, sua média é de \033[1;33m{media}\033[m.\nVocê terá que ficar de "\033[1;33mRECUPERAÇÃO\033[m".'
          f'\nSe esforce mais pra ser "\033[1;34mAPROVADO\033[m" desta vez!')
