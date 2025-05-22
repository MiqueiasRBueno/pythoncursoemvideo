# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(width, length):
    a = width * length
    print(f'A área de um terreno de \033[32m{width}\033[m m X \033[32m{length}\033[m m é de \033[32m{a}\033[m m².')


# Programa principal:
print(f'''\n\033[1;33m{"CONTROLE DE TERRENOS":^50}\033[m
\033[1;32m{"_" * 54}\033[m\n''')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
