# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre
# ele.

while True:
    digite = input('Digite algo: ')
    print(f'É numérico: ', digite.isnumeric())
    print(f'É alfabético? ', digite.isalpha())
    print(f'É alfanumérico? ', digite.isalnum())
    print(f'É capitalizado: ', digite.istitle())
    print(f'É tudo maiúsculo: ', digite.isupper())
    parar = ' '
    while parar not in 'SsNn':
        parar = str(input('\033[33mQuer continuar? [S/N]\033[m ')).upper().strip()[0]
    if parar == 'N':
        break
print('Análise concluída com sucesso!')
