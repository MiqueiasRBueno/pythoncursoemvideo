# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0
for c in range(1, 6):
    peso = float(input(f'O peso da {c}ª pessoa é: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido foi de \033[1;31m{maior_peso:.2f}\033[mkg')
print(f'O menor peso lido foi \033[1;34m{menor_peso:.2f}\033[mkg')
