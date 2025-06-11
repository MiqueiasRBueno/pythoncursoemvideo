# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
print(f'O valor de 100 + 17,5 % é de {moeda.aumentar(100, 17.5)}')
print(f'O valor de 400 - 42,8 % é de {moeda.diminuir(400, 42.8)}')
print(f'A metade de 367 é {moeda.metade(367)}')
print(f'O dobro de 723 é {moeda.dobro(723)}')
