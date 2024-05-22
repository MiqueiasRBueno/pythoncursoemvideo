# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('IGREJA', 'CARRO', 'ARMAZEM', 'ESTUDO', 'AVIAO', 'PASSARO', 'HIPOPOTAMO')
for vg in palavras:
    print(f'\nNa palavra \033[32;1m{vg}\033[m temos as vogais ', end='')
    for vogais in vg:
        if vogais.lower() in 'aeiou':
            print(f'\033[32;1m{vogais}\033[m', end='')
