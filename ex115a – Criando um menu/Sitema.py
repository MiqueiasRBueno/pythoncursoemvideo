from lib.interface import *

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair Do Programa'])
    if resposta == 1:
        cabecalho('opção 1')
    elif resposta == 2:
        cabecalho('opção 2')
    elif resposta == 3:
        cabecalho('Saindo do programa!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
