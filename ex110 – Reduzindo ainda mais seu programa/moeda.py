def aumentar(preco=0, taxa=0, formoeda=False):
    """
    _> Função para acrescentar uma porcentagem em um valor
    :param formoeda: parametro para formatação da moeda
    :param preco: Valor que receberá o aumento
    :param taxa: porcentagem a ser aumentada
    :return: novo valor com o aumento
    """
    res = preco + (preco * taxa/100)
    return res if not formoeda else moeda(res)

def diminuir(preco=0, taxa=0, formoeda=False):
    """
    _> Função para diminuir uma porcentagem em um valor
    :param formoeda: parametro para formatação da moeda
    :param preco: Valor que será subtraído a porcentagem
    :param taxa: Porcentagem que será subtraída do valor
    :return: retorna o novo valor diminuído a porcentagem
    """
    res = preco - (preco * taxa/100)
    return res if not formoeda else moeda(res)

def dobro(preco=0, formoeda=False):
    """
    _> Função que dobra o valor digitado
    :param formoeda: parametro para formatação da moeda
    :param preco: Valor que será dobrado
    :return: retorna o novo valor dobrado
    """
    res = preco * 2
    return res if not formoeda else moeda(res)

def metade(preco=0, formoeda=False):
    """
    _> Função que mostra a metade do valor digitado
    :param preco: Valor digitado pelo usuário
    :param formoeda: Função para formatação de moeda
    :return: metade do valor digitado
    """
    res = preco / 2
    return res if not formoeda else moeda(res)


def moeda(preco, tmoeda='R$'):
    """
    _> Função para formatação monetária
    :param preco: valor monetário
    :param tmoeda: tipo da moeda usada
    :return:
    """
    return f'{tmoeda}{preco:^8.2f}'.replace('.', ',')


def resumo(preco=0, taum=0, tdim=0):
    """
    _> Função para resumir o programa
    :param preco: Preço a ser analisado
    :param taum: Taxa a ser aumentado no preço
    :param tdim: Taxa a ser subtraída do preço
    """
    print(f'''\033[1;31m{"-" * 40}\033[m
{"RESUMO DO PREÇO":^40}
\033[1;31m{"-" * 40}\033[m
{"Preço analisado:":<}{f"{moeda(preco)}":>26}
{"Dobro do preço:":<}{f"{dobro(preco, True)}":>27}
{"Metade do preço:":<}{f"{metade(preco, True)}":>26}
{f"{taum} % de aumento:":<}{f"{aumentar(preco, taum,True)}":>26}
{f"{tdim} % de retirada:":<}{f"{diminuir(preco, tdim, True)}":>25}
\033[1;31m{"-" * 40}\033[m''')
