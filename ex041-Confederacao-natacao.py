# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, conforme a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

idade = int(input('Digite a idade do aluno: '))
if idade <= 9:
    print(f'Você tem \033[1;34m{idade:.0f}\033[m anos, está na categoria \033[1;34mMIRIM\033[m.')
elif 14 >= idade > 9:
    print(f'Você tem \033[1;32m{idade:.0f}\033[m anos, está na categoria \033[1;32mINFANTIL\033[m.')
elif 19 >= idade > 14:
    print(f'Você tem \033[31;1m{idade:.0f}\033[m anos, está na categoria \033[1;31mJUNIOR\033[m.')
elif 25 >= idade > 19:
    print(f'Você tem \033[1;33m{idade:.0f}\033[m anos, está na categoria \033[1;33mSÊNIOR\033[m.')
else:
    print(f'Você tem \033[35;1m{idade:.0f}\033[m anos, está na categoria \033[1;35mMASTER\033[m.')
