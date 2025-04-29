# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('IGREJA', 'CARRO', 'ARMAZÉM', 'ESTUDO', 'AVIÃO', 'PÁSSARO', 'HIPOPÓTAMO')
for vg in palavras:
    print(f'\nNa palavra \033[32;1m{vg}\033[m temos as vogais ', end=' ')
    for vogais in vg:
        if vogais.lower() in 'aeéiíoóu':
            print(f'\033[32;1m{vogais}\033[m', end=' ')
