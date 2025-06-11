def aumentar(preco=0, taxa=0):
    """
    _> Função para acrescentar uma porcentagem em um valor
    :param preco: Valor que receberá o aumento
    :param taxa: porcentagem a ser aumentada
    :return: novo valor com o aumento
    """
    res = preco + (preco * taxa/100)
    return res

def diminuir(preco=0, taxa=0):
    """
    _> Função para diminuir uma porcentagem em um valor
    :param preco: Valor que será subtraído a porcentagem
    :param taxa: Porcentagem que será subtraída do valor
    :return: retorna o novo valor diminuído a porcentagem
    """
    res = preco - (preco * taxa/100)
    return res

def dobro(preco=0):
    """
    _> Função que dobra o valor digitado
    :param preco: Valor que será dobrado
    :return: retorna o novo valor dobrado
    """
    res = preco * 2
    return res

def metade(preco=0):
    """
    _> Função que mostra a metade do valor digitado
    :param preco: Valor digitado pelo usuário
    :return: metade do valor digitado
    """
    res = preco / 2
    return res


def moeda(preco=0, tmoeda='R$'):
    """
    _> Função para formatação monetária
    :param preco: valor monetário
    :param tmoeda: tipo da moeda usada
    :return:
    """
    return f'{tmoeda}{preco:^8.2f}'.replace('.', ',')
