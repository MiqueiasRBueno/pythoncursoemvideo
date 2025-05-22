# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

# Criação de função:
def escreva(txt):
    tam = len(txt) + 4
    print(f'''\033[1;31m{"=" * tam}\033[m
\033[1m{txt.title():^{tam}}\033[m
\033[1;31m{"=" * tam}\033[m''')


# Programa principal:
escreva('olá, mundo')
escreva('miquéias')
escreva('ana beatriz mendes bueno')
escreva('renato mendes bueno')
escreva('silvia letícia r. mendes')
