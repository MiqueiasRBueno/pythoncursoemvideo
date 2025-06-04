# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

# Função
def notas(*num, situ=False):
    """
    — > A função notas é um programa para adicionar a nota de vários alunos
    :param num: recebe os números adicionados
    :param situ: se verdadeiro mostra a situação da média das notas da classe
    :return: retorna um dicionário com os dados adicionados
    """
    resp = {}
    total = 0
    for _ in num:
        total += 1
        resp['Total'] = total
        resp['Maior'] = max(num)
        resp['Menor'] = min(num)
        soma = sum(num)
        media = soma / len(num)
        resp['Média'] = media
        if situ:
            if media < 5:
                resp['Situação'] = 'Ruim!'
            elif media < 7:
                resp['Situação'] = 'Razoável!'
            else:
                resp['Situação'] = 'Boa!'
    return resp


# Programa principal:
resposta = notas(7.5, 5.5, 6, 10, 9, situ=True)
print(resposta)
