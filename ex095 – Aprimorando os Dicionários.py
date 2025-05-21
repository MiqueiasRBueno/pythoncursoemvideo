# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

player_management_dict = dict()
player_management_list = list()
goals_list_management = []
while True:
    player_management_dict['Name'] = str(input('Nome do Jogador e ou Jogadora: ')).title().strip()
    quantity_matches = int(input(f'Quantas partidas {player_management_dict["Name"]} jogou?: '))
    for m in range(0, quantity_matches):
        goals_list_management.append(int(input(f'Quantos gols {player_management_dict["Name"]}'
                                                    f' fez na {m + 1}ª partida?: ')))
        player_management_dict['Goals'] = goals_list_management[:]
        player_management_dict['Total'] = sum(player_management_dict['Goals'])
    player_management_list.append(player_management_dict.copy())
    player_management_dict.clear()
    goals_list_management.clear()
    while True:
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if stop in 'SN':
            break
        print('ERRO! Digite S ou N: ')
    if stop in 'N':
        break
print(f'''\033[1;32m{'-=' * 27}\033[m
{'Cod':<5}_ {'Nome':<20}{'Gols':<15}{'Total':>8}
\033[1;32m{'-' * 50}\033[m''')
for i, p in enumerate(player_management_list):
    print(f' {i:<4}_ {p['Name']:<18}{f'{p['Goals']}':<11}{p['Total']:>10}')
print(f'\033[32m{'-' * 54}\033[m')
while True:
    show_player_data = int(input('Mostrar dados de qual jogador e ou jogadora?: '))
    if show_player_data == 999:
        break    
    if show_player_data >= len(player_management_list):
        print('ERRO! Por favor, escolha um código do jogador na lista!')
    else:
        print(f'__ Levantamento do jogador e ou jogadora \033[1;32m{player_management_list[show_player_data]
        ["Name"]}\033[m: ')
        part = 0
        for g in player_management_list[show_player_data]["Goals"]:
            print(f'Na {1 + part}ª partida \033[1;32m{player_management_list[show_player_data]["Name"]
            }\033[m fez \033[32m{g}'
                  f'\033[m gols')
            part += 1
    print(f'\033[1;32m-\033[m' * 54)
print(f'{"\033[32m<<\033[mVolte Sempre!\033[1;32m>>\033[m":^70}')
