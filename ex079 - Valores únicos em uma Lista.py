#  Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado. No final,
#  serão exibidos todos os valores únicos digitados, em ordem crescente.

listavalores = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num not in listavalores:
        listavalores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
    if parar == 'N':
        break
print('=-' * 30)
listavalores.sort()
print(f'Você digitou os valores {listavalores}')
