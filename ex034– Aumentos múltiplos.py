# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal_func = float(input('Qual o salário do funcionário: '))
sal_min = float(input('Qual valor do salário mínimo? '))
if sal_func <= sal_min:
    nov_sal = sal_func + (sal_func * 0.15)
    print(f'O salário atual do funcionário é de R$\033[1;32m{sal_func:.2f}\033[m\n'
          f'Com o acréscimo de \033[33m15%\033[m passará a ser de R$\033[1;32m{nov_sal:.2f}\033[m')
else:
    nov_sal = sal_func + (sal_func * 0.1)
    print(f'O salário atual do funcionário é de R$\033[1;34m{sal_func:.2f}\033[m\n'
          f'Com o acréscimo de \033[1;33m10%\033[m passará a ser de R$\033[1;34m{nov_sal:.2f}\033[m')
