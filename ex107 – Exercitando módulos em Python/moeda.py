def aumentar(preco, taxa):
    """
    _> Função para acrescentar uma porcentagem em um valor
    :param preco: Valor que receberá o aumento
    :param taxa: porcentagem a ser aumentada
    :return: novo valor com o aumento
    """
    res = preco + (preco * taxa/100)
    return res

def diminuir(preco, taxa):
    """
    _> Função para diminuir uma porcentagem em um valor
    :param preco: Valor que será subtraído a porcentagem
    :param taxa: Porcentagem que será subtraída do valor
    :return: retorna o novo valor diminuído a porcentagem
    """
    res = preco - (preco * taxa/100)
    return res

def dobro(preco):
    """
    _> Função que dobra o valor digitado
    :param preco: Valor que será dobrado
    :return: retorna o novo valor dobrado
    """
    res = preco * 2
    return res

def metade(preco):
    """
    _> Função que mostra a metade do valor digitado
    :param preco: Valor digitado pelo usuário
    :return: metade do valor digitado
    """
    res = preco / 2
    return res
