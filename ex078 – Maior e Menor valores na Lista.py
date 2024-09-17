# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas posições na lista.

valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {c + 1}ª posição: ')))
print(f'Você digitou os {valores}')
print(f'O maior valor digitado foi {max(valores)} na: ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'\033[1;32m{i + 1}\033[m\033[1mª\033[m...', end='')
print('posições')
print(f'O menor valor digitado foi {min(valores)} na: ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'\033[1;32m{i + 1}\033[m\033[1mª\033[m...', end='')
print('posições')

