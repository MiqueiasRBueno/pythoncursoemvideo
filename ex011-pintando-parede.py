# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura de sua parede: '))
altura = float(input('Qual a altura de sua parede: '))
print('Tinta marca "\033[31;1mA\033[m" \033[31;1m3\033[m demãos por metro\n'
      'Tinta marca "\033[1;31mB\033[m" \033[1;31m4\033[m demãos por metro\nTinta marca "\033[1;31mC\033[m" '
      '\033[1;31m6\033[m'
      ' demãos por metro')
marca = input('Qual marca deseja? ').upper()
area = largura * altura
qtinta = area / 2
print(f'A parede a ser pintada tem uma área de \033[32;1m{area:.2f}\033[m metros')
if marca == 'A':
    total = qtinta * 3
    print(f'Serão necessários \033[1;32m{total:.2f}\033[m litro(s) de tinta por demão da marca \033[1;32m{marca}\033[m'
          f' para pinta- lá.')
elif marca == 'B':
    total = qtinta * 4
    print(f'Serão necessários \033[1;32m{total:.2f}\033[m litro(s) de tinta por demão da marca \033[1;32m{marca}\033[m'
          f' para pinta- lá.')
elif marca == 'C':
    total = qtinta * 6
    print(f'Serão necessários \033[1;32m{total:.2f}\033[m litro(s) de tinta por demão da marca \033[1;32m{marca}\033[m'
          f' para pinta- lá.')
