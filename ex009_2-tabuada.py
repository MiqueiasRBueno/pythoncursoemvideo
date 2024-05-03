# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

tab = 0
num = int(input('Digite um número inteiro: '))
while True:
    tab += 1
    print('{: >2}  \033[31m{: ^2}\033[m{: >2}  \033[31m{:^2}\033[m{: >5}'.format(tab, 'X', num, '=', tab * num))
    if tab == 10:
        break
