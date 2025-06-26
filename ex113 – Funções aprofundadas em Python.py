# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    """
    Validador de números inteiros
    :param msg: Dados a serem validados
    :return: Dados validados
    """
    ok = False
    valor = 0
    while True:
        num = str(input(msg)).strip()
        try:
            valor = int(num)
            ok = True
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um valor válido:\033[m ')
        if ok:
            break
    return valor

def leiaFloat(msg):
    """
    Validador de números reais
    :param msg: Dados a serem validados
    :return: Dados validados
    """
    ok = False
    valor = 0
    while True:
        num = str(input(msg)).strip().replace(',', '.')
        try:
            valor = float(num)
            ok = True
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real valido!\033[m')
        if ok:
            break
    return valor


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {inteiro} e o número real foi o {real}')
