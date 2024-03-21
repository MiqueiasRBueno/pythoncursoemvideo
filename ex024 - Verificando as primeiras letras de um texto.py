# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Digite o nome de uma cidade qualquer: ')).strip().upper()
print(nome.split()[0] == 'SANTO')
