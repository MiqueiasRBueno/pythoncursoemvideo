# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('lápis', 1.75,
         'caneta', 3.50,
         'caderno', 12.00,
         'borracha', 2.50,
         'cola', 6.75)
print('-' * 40)
print('{:^48}'.format('\033[34mTABELA DE PREÇOS\033[m'))
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<27}', end='')
    else:
        print(f'R$\033[31m{lista[pos]:>7.2f}\033[m')
print('-' * 40)
