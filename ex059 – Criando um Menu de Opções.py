# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
#  Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
pri_vl = int(input('Primeiro valor: '))
seg_vl = int(input('Segundo valor: '))
terminar = False
while not terminar:
    print('''[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa''')
    opcao = int(input('>>>>>Qual é a sua opção? '))
    print('=-=' * 15)
    if opcao == 5:
        terminar = True
    else:
        if opcao == 1:
            soma = pri_vl + seg_vl
            print(f'A soma entre \033[1;31m{pri_vl} + {seg_vl}\033[m é \033[1;31m{soma}\033[m')
        elif opcao == 2:
            mult = pri_vl * seg_vl
            print(f'O resultado da multiplicação entre \033[1;33m{pri_vl} X {seg_vl}\033[m é \033[1;33m{mult}\033[m')
        elif opcao == 3:
            if seg_vl > pri_vl:
                print(f'Entre {pri_vl} e {seg_vl} o número maior é {seg_vl}')
            else:
                print(f'Entre {pri_vl} e {seg_vl} o número mairo é {pri_vl}')
        elif opcao == 4:
            pri_vl = int(input('Primeiro valor: '))
            seg_vl = int(input('Segundo valor: '))
        else:
            print('Opção inválida. Tente novamente.')
    print('=-=' * 15)
print('Finalizando...')
sleep(3)
print('=-=' * 15)
print('Fim do programa, volte sempre!')
