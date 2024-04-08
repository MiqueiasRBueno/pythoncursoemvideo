# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Insira o primeiro termo de sua P.A.: '))
razao = int(input('Insira a razão para sua P.A.: '))
total = 0  # Será somado ao número de termo inicial com os termos adicionais
mais = 10  # Número de termos da p.a inicial
soma = 0   # somará a repetição + 1
n = 0  # localização do termo da pa
while mais != 0:
    total = total + mais
    while n != total:
        soma += 1
        n += 1
        pa = termo + (n - 1) * razao
        print(pa, end='\033[1;31m ¬ \033[m')
    mais = int(input('\033[1;32mPAUSA\033[m\nQuantos termos você quer mostrar a mais? '))
print('\033[1;31mP.A.\033[m finalizada com \033[1;33m{}\033[m termos mostrados.'.format(soma))
