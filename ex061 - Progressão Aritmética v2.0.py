# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('=-=' * 5, 'Gerador de P.A.', '=-=' * 5)
termo = int(input('Digite o primeiro termo da P.A.: '))
rz = int(input('Qual a razão da P.A.: '))
n = 0
while n < 10:
    n += 1
    pa = termo + (n - 1) * rz
    print(pa, end='\033[1;31m ¬ \033[m')
print('\033[1;32mACABOU\033[m')
