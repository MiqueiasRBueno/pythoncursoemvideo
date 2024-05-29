#  Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado. No final,
#  serão exibidos todos os valores únicos digitados, em ordem crescente.

listavalores = []
novovalor = []
while True:
    listavalores.append(int(input('Digite um valor: ')))
    for elemento in listavalores:
        if elemento not in novovalor:
            novovalor.append(elemento)
            print('Valor adicionado com sucesso...')
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
    if parar == 'N':
        break
print(f'Você digitou os valores {novovalor}')
