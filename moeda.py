def aumentar(n, aum):
    """
    _> Função para acrescentar uma porcentagem em um valor
    :param n: Valor que receberá o aumento
    :param aum: porcentagem a ser aumentada
    :return: novo valor com o aumento
    """
    return n + ((n * aum) / 100)

def diminuir(n, dim):
    """
    _> Função para diminuir uma porcentagem em um valor
    :param n: Valor que será subtraído a porcentagem
    :param dim: Porcentagem que será subtraída do valor
    :return: retorna o novo valor diminuído a porcentagem
    """
    return n - ((n * dim) / 100)

def dobro(n):
    """
    _> Função que dobra o valor digitado
    :param n: Valor que será dobrado
    :return: retorna o novo valor dobrado
    """
    return n * 2

def metade(n):
    """
    _> Função que mostra a metade do valor digitado
    :param n: Valor digitado pelo usuário
    :return: metade do valor digitado
    """
    return n / 2
