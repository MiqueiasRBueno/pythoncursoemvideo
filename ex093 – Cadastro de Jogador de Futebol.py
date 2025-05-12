# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print(f'''\033[1;31m{'-=' * 20}\033[m
{'GERENCIADOR DE JOGADORES':^40}
\033[1;31m{'-=' * 20}\033[m''')
gerenciador_jogador = dict()
qtd_gols = list()
gerenciador_jogador['Nome'] = str(input('Nome do Jogador e ou jogadora: ')).title().strip()
partidas = int(input(f'Quantas partidas {gerenciador_jogador['Nome']} jogou? '))
for c in range(0, partidas):
    qtd_gols.append(int(input(f'Quanto gols {gerenciador_jogador['Nome']} fez na {c + 1}ª partida? ')))
    gerenciador_jogador['Gols'] = qtd_gols
    gerenciador_jogador['Total'] = sum(gerenciador_jogador['Gols'])
print(f'\033[1;31m{'-=' * 20}\033[m')
for k, v in gerenciador_jogador.items():
    print(f'O campo {k} tem o valor \033[1;32m{v}\033[m')
print(f'''\033[1;31m{'-=' * 20}\033[m
O jogador e ou jogadora {gerenciador_jogador['Nome']} jogou {partidas} partidas, e:
\033[1;31m{'-=' * 20}\033[m''')
tot = 0
for g in qtd_gols:
    print(f'_ marcou \033[1;32m{qtd_gols[tot]}\033[m gol(s) na \033[1;32m{g}\033[mª partida ')
    tot += 1
