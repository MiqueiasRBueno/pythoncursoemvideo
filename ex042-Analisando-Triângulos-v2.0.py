# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

frescal = ('\033[1;32m-=-\033[m' * 20)
print(f'{frescal}')
print('\033[1;34mAnalisador de triângulos.\033[m')
print(f'{frescal}')
print('\033[1;34m')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo formado é \033[1;32mEQUILÁTERO\033[m!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('O triângulo formando é \033[1;32mISÓSCELES\033[m!')
    else:
        print('O triângulo formado é \033[32;1mESCALENO\033[m!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
