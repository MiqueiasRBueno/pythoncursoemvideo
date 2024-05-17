# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('ATLÉTICO PARANAENSE', 'BAHIA', 'FLAMENGO', 'BOTAFOGO', 'SÃO PAULO',
         'CRUZEIRO', 'ATLÉTICO MINEIRO', 'BRAGANTINO', 'PALMEIRAS', 'INTERNACIONAL',
         'FORTALEZA', 'GRÊMIO', 'VASCO', 'CRICIÚMA', 'JUVENTUDE',
         'CORINTHIANS', 'FLUMINENSE', 'VITÓRIA', 'ATLÉTICO GOIÂNO', 'CUÍABA')
print('\033[1;33m-=-\033[m' * 53)
print('\033[1;31m{:^150}\033[m'.format('LISTA DE TIMES DO BRASILEIRÃO'))
print(times)
print('\033[1;33m-=-\033[m' * 53)
print('\033[1;31m{:^150}\033[m'.format('OS 5 PRIMEIROS TIMES DO BRASILEIRÃO'))
print(times[0:5])
print('\033[1;33m-=-\033[m' * 53)
print('\033[1;31m{:^150}\033[m'.format('OS 4 ÚLTIMOS COLOCADOS'))
print(times[-4:20])
print('\033[1;33m-=-\033[m' * 53)
print('\033[1;31m{:^150}\033[m'.format('OS TIMES DO BRASILEIRÃO EM ORDEM ALFABÉTICA'))
print(sorted(times))
print('\033[1;33m-=-\033[m' * 53)
print('\033[1;31m{:^150}\033[m'.format('POSIÇÃO DO CORINTHIANS NO CAMPEONATO'))
print(f'O Corinthians esta na {times.index('CORINTHIANS') + 1}ª posição')
print('\033[1;33m-=-\033[m' * 53)
