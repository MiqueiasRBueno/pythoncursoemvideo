num = int(input('Digite um número inteiro: '))
qtd = 0
num_zero = 0
for c in range(1, num + 1):
    primo = num % c
    if primo == 0:
        qtd += 1
        num_zero = qtd == 2
if num_zero:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é um número primo!')
