# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
soma = 0
while True:
    num = int(input('Digite um valor inteiro:>'))
    lista.append(num)
    lista.sort(reverse=True)
    soma += 1
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar?>[S/N] ')).upper().strip()[0]
    if parar == 'N':
        break
print(f'Foram digitados {soma} números nessa lista.')
print(f'Os valores digitados em ordem decrescente foram {lista}')
