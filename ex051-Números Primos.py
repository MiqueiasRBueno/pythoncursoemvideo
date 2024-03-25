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
    print(f'O número \033[1;31m{num}\033[m é um número \033[32;1mPRIMO\033[m!')
else:
    print(f'O número \033[1;31m{num}\033[m não é um número \033[1;32mPRIMO\033[m!')
