# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# Função:
def voto(dt_nasc):
    """
    Função para análise da obrigatóriedade de votar
    :param dt_nasc: recebe o ano de nascimento 
    :return: retorna mensagem NEGADO, OPCIONAL ou OBRIGATÓRIO conforme a idade
    """
    from datetime import datetime

    ano = datetime.now().year
    idade = ano - dt_nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade <= 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# Programa Principal:
nascimento = int(input('Digite o ano de seu nascimento: '))
print(voto(nascimento))
