# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = dict()
boletim['nome'] = str(input('Nome: ')).title().strip()
boletim['média'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['média'] >= 7:
    boletim['situação'] = 'Aprovado'
elif 5 < boletim['média'] < 7:
    boletim['situação'] = 'Recuperação'
else:
    boletim['situação'] = 'Reprovado'
print(f'\033[1;31m{'=' * 55}\033[m')
for k, v in boletim.items():
    print(f'- {f'{k}'.title()} é igual a {v}')
print(f'\033[1;31m{'=' * 55}\033[m')
