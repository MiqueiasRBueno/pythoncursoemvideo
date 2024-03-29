# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

print('\033[1;32m=' * 7, '\033[mANALISANDO TRIÂNGULOS', '\033[1;32m=' * 7, '\033[m')
seg_1 = int(input('Digite o valor do 1º seguimento: '))
seg_2 = int(input('Digite o valor do 2º segmento: '))
seg_3 = int(input('Digite o valor do 3º segmento: '))
if seg_1 + seg_2 > seg_3 and seg_1 + seg_3 > seg_2 and seg_2 + seg_3 > seg_1:
    print(f'Os segmentos digitados FORMAM um triângulo!')
    if seg_1 != seg_2 != seg_3 != seg_1:
        print(f'Temos um triângulo \033[1;31mESCALENO\033[m!')
    if seg_1 == seg_2 == seg_3 == seg_1:
        print(f'Temos um triângulo \033[1;33mEQUILÁTERO\033[m!')
    if seg_1 != seg_2 == seg_3 != seg_1:
        print(f'Temos um triângulo \033[1;35mISÓSCELES\033[m!')
