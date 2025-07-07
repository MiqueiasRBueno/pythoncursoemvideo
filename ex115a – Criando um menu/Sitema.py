from libe.interface import *
from libe.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair Do Programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        cadastrar_usuario(arq, name=str(input('Nome: ')), idade=int(input('Idade: ')))
    elif resposta == 3:
        cabecalho('Saindo do programa!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
