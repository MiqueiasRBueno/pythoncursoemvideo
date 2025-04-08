# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
frase_join = frase.strip().replace(' ', '')
frase_invertida = ''.join(reversed(frase_join))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
if frase_join == frase_invertida:
    print(f' O inverso de \033[1;33m{frase_join}\033[m é \033[1;33m{frase_invertida}\033[m.'
          f'\n Temos um \033[1;32mPALÍNDROMO\033[m!')
else:
    print(f'O inverso de \033[1;33m{frase_join}\033[m é \033[1;31m{frase_invertida}\033[m!'
          f'\nA frase digitada não é um \033[1;32mPALÍNDROMO\033[m! ')
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'\033[1;32m{frase_invertida}\033[m é um palíndromo!')
else:
    print(f'\033[1;34m{frase_invertida}\033[m não é um palíndromo!')
