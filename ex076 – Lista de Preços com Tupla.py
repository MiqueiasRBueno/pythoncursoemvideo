# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('lápis............................R$ \033[31m1,75\033[m',
         'caneta...........................R$ \033[31m3,50\033[m',
         'caderno..........................R$\033[31m12,00\033[m',
         'borracha.........................R$ \033[31m2,50\033[m',
         'cola.............................R$ \033[31m6,75\033[m')
print('-' * 40)
print('{:^48}'.format('\033[31mTABELA DE PREÇOS\033[m'))
print('-' * 40)
for ob in lista:
    print(ob)
print('-' * 40)
