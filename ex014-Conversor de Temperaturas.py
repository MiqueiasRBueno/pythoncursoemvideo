# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite uma temperatura em graus celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'Temperatura digitada em celsius: \033[1;32m{celsius:.2f}\033[m °C'
      f'\nTemperatura convertida em fahrenheit: \033[1;36m{fahrenheit:.2f}\033[m °F')
