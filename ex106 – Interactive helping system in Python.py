# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

#Função:
def interHelp():
    """
    — > Um mini-sistema que utilize o Interactive Help do Python.
    O usuário vai digitar o comando e o manual vai aparecer.
    Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
    :return:
    """
    from time import sleep
    print(f'''\033[1;42m{"=" * 40}
{"SISTEMA DE AJUDA PYTHON":^40}
{"=" * 40}
\033[m''', end='')
    while True:
        ajuda = str(input('Função ou Biblioteca>> '))
        if ajuda in 'fim':
            break
        print(f'''\033[1;43m{"=" * 40}
{f"ACESSANDO DOCUMENTAÇÃO DE '{ajuda}'":^40}
{"=" * 40}
\033[m\033[40;7m''', end='')
        help(ajuda)
        print('\033[m', end='')
    print(f'''\033[1;41m{"=" * 40}
{"ATÉ LOGO!":^40}
{"=" * 40}
\033[m''')

#Programa principal:
interHelp()
