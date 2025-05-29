# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(dt_nasc):
    """
    Função para análise da obrigatóriedade de votar
    :param dt_nasc: recebe o ano de nascimento 
    :return: retorna mensagem NEGADO, OPCIONAL ou OBRIGATÓRIO conforme a idade
    """
    from datetime import datetime

    ano = datetime.now().year
    idade = ano - dt_nasc
    msg = ' '
    if 65 > idade > 18:
        msg = 'VOTO OBRIGATÓRIO!'
    elif 95 > idade > 65 or idade < 16:
        msg = 'VOTO OPCIONAL!'
    elif idade > 95:
        msg = 'VOTO NEGADO!'
    return msg

dt_nasc = int(input('Digite o ano de seu nascimento: '))
print(voto(dt_nasc))