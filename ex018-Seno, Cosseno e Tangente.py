# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
grau = float(input('Digite o valor de um ângulo desejado: '))
print(f'O ângulo de {grau} tem:'
      f'\nSeu radiano {radians(grau):.2f}'
      f'\nSeu seno {sin(radians(grau)):.2f}'
      f'\nE seu cosseno {cos(radians(grau)):.2f}'
      f'\nE sua tangente é {tan(radians(grau)):.2f}')
