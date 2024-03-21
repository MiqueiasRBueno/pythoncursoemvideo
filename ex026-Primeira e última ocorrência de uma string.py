# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
letra = str(input('Digite a letra que deseja analisar: ')).strip().upper()
print('A letra {} aparece {} veze(s) na frase'.format(letra, frase.count(letra)))
print('A primeira aparição da letra {} acontece em {}'.format(letra, frase.find(letra)+1))
print('A sua última aparição é a {}'.format(frase.rfind(letra)+1))
