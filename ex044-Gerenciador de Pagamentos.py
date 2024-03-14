# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
cor = dict(fim='\033[m', verm='\033[1;31m', verd='\033[1;32m', amar='\033[1;33m', azul='\033[1;34m', roxo='\033[1;35m',
           cyan='\033[1;36m', cinza='\033[1;37m')
print(f'{cor['verd']}-=-' * 5, f'{cor['fim']}{cor['azul']}LOJAS PERDIDIMMM{cor['fim']}', f'{cor['verd']}-=-' * 5,
      f'{cor['fim']}')
print('')
valor = float(input('Valor das compras: R$ '))
print('')
print(f'{cor['verd']}-=-' * 4, f'{cor['fim']}{cor['amar']}CONDIÇÃO DE PAGAMENTO:{cor['fim']}', f'{cor['verd']}-=-' * 4,
      f'{cor['fim']}')
print('')
print('[ 1 ] - à vista no dinheiro/ pix: 10% de desconto'
      '\n[ 2 ] - à vista no cartão: 5% de descont'
      '\n[ 3 ] - em até 2x no cartão: preço formal'
      '\n[ 4 ] - em 3x ou mais no cartão: 20% de juros')
opcao = int(input('Opção escolhida: '))
print('')
print(f'{cor['verd']}-=-' * 6, f'{cor['fim']}{cor['verm']}TOTAL A PAGAR{cor['fim']}', f'{cor['verd']}-=-' * 6,
      f'{cor['fim']}')
print('')
if opcao == 1:
    desc = valor - (valor * 0.1)
    print(f'O valor de sua compra é de R$ {valor:.2f}')
    print(f'Total a pagar R$ {desc:.2f}, parabéns, você ganhou um desconto!')
elif opcao == 2:
    desc = valor - (valor * 0.05)
    print(f'O valor de sua compra é de R$ {valor:.2f}')
    print(f'Total a pagar R$ {desc:.2f}, parabéns, você ganhou um desconto!')
elif opcao == 3:
    parc = valor / 2
    print(f'O valor total a pagar por sua compra é de R$ {valor:.2f}')
    print(f'Valor da parcela R$ {parc:.2f}')
else:
    parc = int(input('Entre 3X à 10X, qual a quantidade de parcelas? '))
    juros = valor + (valor * 0.2)
    valor_parc = (juros / parc)
    print(f'O valor de sua compra é de R$ {valor:.2f}')
    print(f'Total a pagar R$ {juros:.2f}, com acréscimo do parcelamento!')
    print(f'Valor das parcelas R$ {valor_parc:.2f}')
print('')
print('Agradeço a preferência, VOLTE SEMPRE!')
