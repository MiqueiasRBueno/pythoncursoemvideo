# Escreva um programa que leia dois números inteiros e compare os, mostrando uma mensagem na tela:
# - O primeiro número é maior
# - O segundo número é maior
# - Não existe número maior, os dois são iguais

num1 = int(input('Digite um número qualquer: '))
num2 = int(input('Digite outro número qualquer: '))
if num1 > num2:
    print('O \033[1;33mprimeiro valor\033[m é \033[1;34mmaior\033[m')
elif num1 < num2:
    print('O \033[1;33msegundo valor\033[m é \033[1;34mmaior\033[m')
else:
    print('Não \033[1;33mexiste valor\033[m maior, os dois são \033[1;34miguais\033[m')
