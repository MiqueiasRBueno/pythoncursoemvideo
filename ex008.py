# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e metros.

medi = float(input('Digite um valor qualquer em metros: '))
print(f'Metros em Kilometros: \033[1;33m{medi / 1000:.2f} km\033[m')
print(f'Metros em Hectómetros: \033[31;1m{medi / 100:.2f} hm\033[m')
print(f'Metros em Decâmetros: \033[32;1m{medi / 10:.2f} dm\033[m')
print(f'Metros digitado: \033[1;34m{medi:.1f} m\033[m')
print(f'Metros em Decímetros: \033[35;1m{medi * 10} dm\033[m')
print(f'Metros em Centímetros: \033[1;36m{medi * 100} cm\033[m')
print(f'Metros em Milímetros: \033[37;1m{medi * 1000} mm\033[m')
