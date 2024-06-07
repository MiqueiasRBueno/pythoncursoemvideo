# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
valor = 0
while True:
    valor += 1
    num = int(input(f'Digite o {valor}º valor:\033[1;31m>\033[m'))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 != 0:
        impares.append(num)
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar? [S/N]\033[1;31m>\033[m')).upper().strip()[0]
    if parar == 'N':
        break
print(f'Todos os valores digitados em nossa lista são:\033[1;31m>\033[m{lista}')
print(f'Todos os valores pares digitados em nossa lista são:\033[1;31m>\033[m{pares}')
print(f'Todos os valores impares digitados em nossa lista são:\033[1;31m>\033[m{impares}')
