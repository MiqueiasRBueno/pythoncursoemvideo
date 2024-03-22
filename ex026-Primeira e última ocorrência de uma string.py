# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
letra = str(input('Digite a letra que deseja analisar: ')).strip().upper()
print('A letra \033[1;34m{}\033[m aparece \033[1;34m{}\033[m veze(s) na frase'.format(letra, frase.count(letra)))
print('A primeira aparição da letra \033[1;32m{}\033[m é na posição '
      '\033[1;32m{}\033[m'.format(letra, frase.find(letra)+1))
print('A sua última aparição é a \033[1;32m{}\033[m'.format(frase.rfind(letra)+1))
