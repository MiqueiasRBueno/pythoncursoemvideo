def leiaInt(msg):
    """
    Validador de números inteiros
    :param msg: Dados a serem validados
    :return: Dados validados
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um valor válido:\033[m ')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse valor!')
            return 0
        else:
            return num
def linhas(tam=42):
    return '\033[31m=\033[m' * tam

def cabecalho(txt):
    print(linhas())
    print(txt.center(42))
    print(linhas())

def menu(listas):
    cabecalho('Menu Principal')
    c = 1
    for item in listas:
        print(f'\033[33m{c} - \033[m\033[34m{item}\033[m')
        c += 1
    print(linhas())
    opc = leiaInt('Sua Opção: ')
    return opc
