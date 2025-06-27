# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    """
    Validador de números inteiros
    :param msg: Dados a serem validados
    :return: Dados validados
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um valor válido:\033[m ')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse valor!')
            return 0
        else:
            return num

def leiaFloat(msg):
    """
    Validador de números reais
    :param msg: Dados a serem validados
    :return: Dados validados
    """
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse valor!')
            return 0
        else:
            return num


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {inteiro} e o número real foi o {real}')
