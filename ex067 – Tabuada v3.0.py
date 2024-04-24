# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

mult = 0

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    mult += 1
    print(f'{num} X {mult} = {mult * num}')
