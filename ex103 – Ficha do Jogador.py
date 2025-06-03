# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e 
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

# Função:
def ficha(name='<desconhecido>', goals=0):
    print(f'O jogador(a) {name} fez {goals} no campeonato!')

# Programa principal:
player_name = str(input('Nome do Jogador(a): ')).title().strip()
num_goals = str(input('Número de gols: '))
if num_goals.isnumeric():
    num_goals = int(num_goals)
else:
    num_goals = 0
if player_name.strip() == '':
    ficha(goals = num_goals)
else:
    ficha(player_name, num_goals)
    