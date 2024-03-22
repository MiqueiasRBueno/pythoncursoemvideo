# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

print('\033[32;1m=' * 40, '\033[m')
print('10 termos de um P.A:')
print('\033[32;1m=' * 40, '\033[m')
termo = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão da P.A: '))
n1 = int(input('Posição do termo na P.A: '))
for n in range(1, 11):
    pa = termo + (n - 1) * rz
    print('\033[33;1m', pa, '\033[m', end='->')
print('\033[36;1mACABOU!\033[m')
pan = termo + (n1-1) * rz
print(f'\n{pan}')
