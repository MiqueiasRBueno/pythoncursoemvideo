# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Digite o valor de seu produto: '))
print('1 - Pagamento com cartão de crédito + 5%\n2 - Pagamento com cartão de débito + 2.5%\n3 - Pagamento à vista, pix'
      ' ou dinheiro, - 5%')
pagamento = int(input('Como deseja efetuar o pagamento: '))
print(f'O valor atual do produto é R$ \033[32;1m{valor:.2f}\033[m')
if pagamento == 1:
    valcard = valor + (valor * 5) / 100
    print('O valor para pagamento com cartão de crédito terá um acréscimo de \033[1;31m5%\033[m')
    print(f'Valor com acréscimo ficará R$ \033[1;31m{valcard:.2f}\033[m')
elif pagamento == 3:
    novvalor = valor - (valor * 5) / 100
    print(f'\nO valor para pagamento à vista, pix ou dinheiro,\n tem um desconto de \033[1;34m5%\033[m'
          f'e fica por apenas R$ \033[32;1m{novvalor:.2f}\033[m')
elif pagamento == 2:
    valcardb = valor + (valor * 2.5) / 100
    print('O valor para pagamento com cartão de débito,\n tem acréscimo de + \033[31;1m2.5%\033[m')
    print(f'Valor com acréscimo ficará apenas R$ \033[1;31m{valcardb:.2f}\033[m')
