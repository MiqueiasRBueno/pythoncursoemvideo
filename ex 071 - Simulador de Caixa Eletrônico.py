print('=' * 40)
print('{:^48}'.format('\033[31;1mBANCO PERDIDIMMM\033[m'))
print('=' * 40)
valor = int(input('Qual valor do seu saque? R$'))
total = valor
cedulas = 200
totced = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedulas}')
        elif cedulas == 200:
            cedulas = 100
        elif cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        elif cedulas == 2:
            cedulas = 1
        totced = 0
        if total == 0:
            break
print('=' * 40)
print("Volte sempre ao BANCO PERDIDIMMM! Volte sempre!")
