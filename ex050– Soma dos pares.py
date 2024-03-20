# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma dos \033[1;34m{cont}\033[m valore(s) pare(s) é \033[1;34m{soma}\033[m')
