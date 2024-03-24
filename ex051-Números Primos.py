from time import sleep
num = int(input('Digite um número inteiro: '))
qtd = 0
num_zero = 0
print('PROCESSANDO...')
sleep(1)
for c in range(1, num + 1):
    primo = num % c
    if primo == 0:
        qtd += 1
if qtd == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é um número primo!')
