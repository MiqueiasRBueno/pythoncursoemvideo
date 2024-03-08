#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
#  alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
#  também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
import math

dia_nas = int(input('Que dia você nasceu? '))
mes_nas = int(input('Em que mês você nasceu?'))
ano_nas = int(input('E em qual ano você nasceu?'))
dt = datetime.date.today()
data_nascimento = datetime.date(ano_nas, mes_nas, dia_nas)
diferenca = dt - data_nascimento
dia = diferenca.days
anos = dia / 365.25
ida_for = math.floor(anos)
if ida_for == 18:
    print(f'Você completará \033[1;32m{ida_for}\033[m este ano.'
          f'\nEstá em período de alistamento militar.\n\033[1;40;7m'
          f' Procure o exército ou a junta militar da sua cidade,'
          f' entre 1° '
          'de janeiro e 30 de junho. \033[m')
elif ida_for < 18:
    print(f'Você tem apenas \033[1;33m{ida_for}\033[m ainda não atingiu a idade para o alistamento militar.'
          f'\nAguarde até o ano que completa 18 anos e procure '
          'o\n\033[1;40;7m exército ou a junta militar de sua cidade, entre 1° de janeiro e 30 de junho. \033[m')
else:
    print(f'Você tem \033[1;31m{ida_for}\033[m anos.'
          f'\nA idade máxima para o alistamento varia de acordo com a situação do cidadão:'
          f'\n\033[1;33m45 anos:\033[m Para brasileiros natos ou naturalizados que não tenham se alistado no ano em '
          f'que completaram 18 anos.'
          f'\n\033[1;33m35 anos:\033[m Para brasileiros natos ou naturalizados que perderam o prazo de alistamento'
          f' e desejam'
          f' ingressar nas Forças Armadas.'
          f'\n\033[1;33m24 anos:\033[m Para portadores de necessidades especiais.'
          f'\nSe você se enquadra em alguma das situações acima:\n\033[1;40;7m Compareça ao exército ou a junta militar'
          f' de sua cidade. \033[m')
