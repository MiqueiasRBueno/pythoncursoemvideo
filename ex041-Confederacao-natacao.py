# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, conforme a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

import datetime
import math

dia_nas = int(input('Dia nascimento do aluno: '))
mes_nas = int(input('Mês nascimento do aluno: '))
ano_nas = int(input('Ano nascimento do aluno: '))
data = datetime.date.today()
dtnasc = datetime.date(ano_nas, mes_nas, dia_nas)
diferenca = data - dtnasc
dia = diferenca.days
ano = dia / 365.25
ida_for = math.floor(ano)
if ida_for <= 9:
    saldo = 9 - 1
    print(f'Você tem \033[1;34m{ida_for:.0f}\033[m ano(s), está na categoria \033[1;34mMIRIM\033[m.')
    print(f'Falta \033[1;34m{saldo:.0f}\033[m ano(s) para você entrar na categoria \033[1;34mINFANTIL\033[m.')
elif 14 >= ida_for > 9:
    saldo = 14 -1
    print(f'Você tem \033[1;32m{ida_for:.0f}\033[m ano(s), está na categoria \033[1;32mINFANTIL\033[m.')
    print(f'Falta \033[1;32m{saldo:.0f}\033[m ano(s) para entrar na categoria \033[1;32mJUNIOR\033[m')
elif 19 >= ida_for > 14:
    saldo = 19 - 1
    print(f'Você tem \033[31;1m{ida_for:.0f}\033[m ano(s), está na categoria \033[1;31mJUNIOR\033[m.')
    print(f'Falta \033[1;31m{saldo:.0f}\033[m ano(s) para entrar na categoria \033[1;31mSÊNIOR\033[m.')
elif 25 >= ida_for > 19:
    saldo = 25 -1
    print(f'Você tem \033[1;33m{ida_for:.0f}\033[m ano(s), está na categoria \033[1;33mSÊNIOR\033[m.')
    print(f'Falta \033[1;33m{saldo:.0f}\033[m ano(s) para entrar na categoria \033[1;33mMASTER\033[m.')
else:
    print(f'Você tem \033[35;1m{ida_for:.0f}\033[m ano(s), está na categoria \033[1;35mMASTER\033[m.')
