# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

vel_atual = float(input('Qual a velocidade atual do carro? '))
if vel_atual <= 80:
    print('\033[1;32mTenha um bom dia, DIRIJA COM SEGURANÇA!\033[m')
else:
    valor = (vel_atual - 80) * 7
    print('\033[1;31mMULTADO!\033[m Você excedeu o limite de velocidade que é de'
          ' \033[1;31m80\033[mkm/h')
    print(f'Você deve pagar uma multa de R$\033[1;33m{valor:.2f}\033[m')
    print('\033[32;1mTenha um bom dia, DIRIJA COM SEGURANÇA!\033[m')
