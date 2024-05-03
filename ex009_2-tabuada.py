# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

while True:
    num = int(input('Digite um número inteiro: '))
    for tab in range(1, 11):
        print('{: >2}  \033[31m{: ^2}\033[m{: >2}  \033[31m{:^2}\033[m{: >5}'.format(tab, 'X', num, '=', tab * num))
    parar = ' '
    while parar not in 'SsNn':
        parar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if parar == 'N':
        break
print('Tabuada finalizada com sucesso!')
