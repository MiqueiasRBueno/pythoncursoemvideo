# Crie um programa de interação com seus filhos.

cor = dict(fim='\033[m', vermelho='\033[1;31m', verde='\033[1;32m', amarelo='\033[1;33m', azul='\033[1;34m',
           roxo='\033[1;35m', cian='\033[1;36m', cinza='\033[1;37m', inver='\033[1;7;32;40m')
divisao = (f'{cor['amarelo']}-=-{cor['fim']}' * 20)
nome = str(input(f'{cor['cian']}Qual é o seu primeiro nome? ')).strip().title()
nome_m = str(input('Qual é seu nome do meio? ')).strip().title()
sobrenome = str(input('E seu sobrenome, qual é? ')).strip().title()
cor1 = str(input('Que cor você quer que apareça seu primeiro nome? '))
cor2 = str(input('E a cor do seu segundo nome, qual será? '))
cor3 = str(input(f'Agora escolha a cor de seu sobrenome!{cor['fim']} '))
print(divisao)
print(f'{cor[f'{cor1}']}{nome}{cor['fim']} {cor[f'{cor2}']}{nome_m}{cor['fim']} '
      f'{cor[f'{cor3}']}{sobrenome}{cor['fim']}')
print(divisao)
print(f'{cor['inver']}Que lindo que seu nome ficou!{cor['fim']}')
