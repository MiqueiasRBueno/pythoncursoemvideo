# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas posições na lista.

valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {c + 1}ª posição: ')))
print(f'Você digitou os {valores}')
print(f'O maior valor digitado foi {max(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i + 1}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i + 1}...', end='')
print()
