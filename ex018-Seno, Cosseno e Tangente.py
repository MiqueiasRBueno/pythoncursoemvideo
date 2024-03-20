# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos
grau = float(input('Digite o valor de um ângulo desejado: '))
rd = radians(grau)
sen = sin(rd)
cos = cos(rd)
print(f'O ângulo de {grau} tem:'
      f'\nSeu radiano {rd:.2f}'
      f'\nSeu seno {sen:.2f}'
      f'\nE seu cosseno {cos:.2f}')
