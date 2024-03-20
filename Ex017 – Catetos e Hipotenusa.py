# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

cateto_op = int(input('Digite um valor: '))
cateto_adj = int(input('Digite outro valor: '))
hipotenusa = (cateto_op ** 2 + cateto_adj ** 2)**0.5
print(f'Um triângulo cujo cateto oposto mede \033[1;31m{cateto_op}\033[m e seu cateto adjacente mede '
      f'\033[1;31m{cateto_adj}\033[m\n'
      f' A hipotenusa mede \033[1;33m{hipotenusa:.2f}\033[m')
