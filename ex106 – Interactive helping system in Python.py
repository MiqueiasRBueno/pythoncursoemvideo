# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

#Função:
def interHelp(txt):
    from time import sleep
    while True:
        print(f'''\033[1;32;40m{"." * 45}
{"SISTEMA DE AJUDA PYTHON HELP":^45}
{"." * 45}
\033[m''', end='')
        sleep(0.5)
        hp = str(input(txt))
        if hp in 'fim':
            print(print(f'''\033[1;31;7m{"." * 45}
{"ATÉ LOGO!":^45}
{"." * 45}
\033[m'''))
            break
        sleep(0.5)
        print(f'''\033[1;33;7m{"." * 45}
    {"ACESSANDO DOCUMENTAÇÃO DO COMANDO":^45}
{"." * 45}
\033[m\033[7m''')
        sleep(0.5)
        help(hp)
    return hp


#Programa principal:
ajuda = interHelp('Função ou Biblioteca> ')
print(ajuda)
