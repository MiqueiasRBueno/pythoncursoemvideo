#  Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
#  quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

cor = dict(fim='\033[m', verde='\033[1;32m', azul='\033[1;34m', amarelo='\033[1;33m')
print(f'{cor['amarelo']}-=-' * 4, f'{cor['fim']}{cor['azul']}LOCADORA PERDIDIMMM{cor['fim']}',
      f'{cor['amarelo']}-=-' * 4, f'{cor['fim']}')
print('')
distancia = int(input('Digite a distância percorrido: (km) '))
dias_locado = int(input('Digite a quantidade de dias locados: (Dias) '))
valor_km = distancia * 0.15
valor_dias = dias_locado * 60
total = valor_km + valor_dias
print('')
print(f'{cor['amarelo']}-=-' * 5, f'{cor['fim']}{cor['azul']}TOTAL A PAGAR{cor['fim']}',
      f'{cor['amarelo']}-=-' * 5, f'{cor['fim']}')
print('')
print(f'Valor a ser pago sobre a distância percorrida R$ {cor['amarelo']}{valor_km:.2f}{cor['fim']}')
print(f'Valor a ser pago sobre as diárias R$ {cor['amarelo']}{valor_dias:.2f}{cor['fim']}')
print(f'Total a ser pago R$ {cor['azul']}{total:.2f}{cor['fim']}')
