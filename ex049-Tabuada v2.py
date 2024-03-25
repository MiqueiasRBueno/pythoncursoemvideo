# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

from time import sleep
num = int(input('Digite um número: '))
print(f'A tabuada de \033[1;31m{num}\033[m de 1 a 10 é:')
for mult in range(1, 11):
    tab = mult * num
    print(mult, 'X', num, '=', tab)
    sleep(0.75)
print(f'Agora você acabou de conhecer a tabuada de \033[1;42;30m {num} \033[m!')
for mult in range(1, 11):
    print(f'{num} X {mult} = {num * mult} ')
    sleep(0.75)