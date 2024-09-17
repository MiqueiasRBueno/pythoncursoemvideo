# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas posições na lista.

lista_num = []
maior = menor = 0
for n in range(0,5):
    lista_num.append(int(input(f'Digite um valor para {n + 1}ª posição : ')))
    if n == 0:
        maior = menor = lista_num[n]
    else:
        if lista_num[n] > maior:
            maior = lista_num[n]
        if lista_num[n] < menor:
            menor = lista_num[n]
print(f'Você digitou os valores: {lista_num}')
print(f'Os maiores valores digitados foram {maior} nas posições: ', end=' ')
for i, v in enumerate(lista_num):
    if v == maior:
        print(f'{i + 1}º...', end=' ')
print()
print(f'Os menores valores digitados foram {menor} nas posições: ', end=' ')
for i, v in enumerate(lista_num):
    if v == menor:
        print(f'{i + 1}ª...', end=' ')
print()