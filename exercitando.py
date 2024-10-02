from random import randint

qtd = int(input('Quantos jogos quer que eu sorteie: '))
total = 1
while total <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        cont += 1
        if cont >= 6:
            break
    total += 1
    print(num)
