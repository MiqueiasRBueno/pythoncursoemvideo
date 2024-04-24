# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

while True:
    print('-' * 40)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if num <= 0:
        break
    for c in range(1, 11):
        print(f'{num} \033[31mX\033[m {c} \033[31m=\033[m {num * c}')
print('Tabuada finalizada com sucesso, volte sempre!')
