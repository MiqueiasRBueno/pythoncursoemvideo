# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# Função criada para calcular o fatorial de um número:
def fatorial(num, show=False):
    """
    — > Função usada para fotorial de um número.
    :param num: Recebe o número que será fatoriado
    :param show: Parâmetro opcional que mostra a multiplicação do número
    :return: retorna o fatorial do número
    """
    fat = 1
    if show:
        print(f'{num}! =', end=' ')
    for f in range(num, 0, -1):
        fat *= f
        if show:
            print(f, end=' ')
            if f > 1:
                print('X', end=' ')
            else:
                print('=', end=' ')
    return fat



# Programa Principal:
print(fatorial(5, True))
print(help(fatorial))
