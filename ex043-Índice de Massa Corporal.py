# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

cor = dict(fim='\033[m', verm='\033[1;31m', verd='\033[1;32m', amar='\033[1;33m', azul='\033[1;34m', roxo='\033[1;35m',
           cyan='\033[1;36m', inver='\033m[1;37m')
peso = float(input('Qual seu peso atual? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu imc atual é de {cor['verm']}{imc:.2f}{cor['fim']}')
    print(f'Você está {cor['verm']}ABAIXO DO PESO{cor['fim']}!')
elif 25 > imc >= 18.5:
    print(f'Seu imc atual é de {cor['azul']}{imc:.2f}{cor['fim']}')
    print(f'Você está com peso {cor['azul']}IDEAL{cor['fim']}!')
elif 30 > imc >= 25:
    print(f'Seu imc atual é de {cor['amar']}{imc:.2f}{cor['fim']}!')
    print(f'Você está em {cor['amar']}SOBREPESO{cor['fim']}!')
elif 40 > imc >= 30:
    print(f'Seu imc atual é de {cor['verm']}{imc:.2f}{cor['fim']}')
    print(f'Você está {cor['verm']}OBESO{cor['fim']}!')
else:
    print(f'Seu imc atual é de {cor['roxo']}{imc:.2f}{cor['fim']}')
    print(f'Você corre risco de morte, está com {cor['roxo']}OBESIDADE MÓRBIDA{cor['fim']}!')
