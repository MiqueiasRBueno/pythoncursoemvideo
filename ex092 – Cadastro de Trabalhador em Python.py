#  Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#  Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from _datetime import datetime
cad_trabalho = dict()
cad_trabalho['Nome'] = str(input('Nome: ')).title().strip()
ano_nasc = int(input('Ano de Nascimento: '))
cad_trabalho['Idade'] = datetime.now().year - ano_nasc
cad_trabalho['CTPS'] = int(input('Carteira de Trabalho (0 Não Tem): '))
if cad_trabalho['CTPS'] != 0:
    cad_trabalho['Contratação'] = int(input('Ano de Contratação: '))
    cad_trabalho['Sálario'] = float(input('Sálario: R$ '))
    cad_trabalho['Aposentadoria'] = cad_trabalho['Idade'] + ((cad_trabalho['Contratação'] + 35) - datetime.now().year)
print('\033[1;31m=\033[m' * 40)
for k, v in cad_trabalho.items():
    print(f'- {k} tem o valor {v}')
