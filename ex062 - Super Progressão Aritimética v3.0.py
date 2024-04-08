# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Insira o primeiro termo de sua P.A.: '))
razao = int(input('Insira a razão para sua P.A.: '))
total = 0
mais = 10
soma = 0
n = 0
while mais != 0:
    total = total + mais
    while n != total:
        soma += 1
        n += 1
        pa = termo + (n - 1) * razao
        print(pa, end='\033[1;31m ¬ \033[m')
    mais = int(input('\033[1;32mPAUSA\033[m\nQuantos termos você quer mostrar a mais? '))
print('P.A. finalizada com \033[1;33m{}\033[m termos mostrados.'.format(soma))
