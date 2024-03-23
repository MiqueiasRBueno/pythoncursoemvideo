num = int(input('Digite um número inteiro: '))
for c in range(1, num + 1):
    c = num % c
    print(c, end=' ')
