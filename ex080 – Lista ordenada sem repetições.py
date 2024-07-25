# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()
for c in range(0, 5):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num not in lista:
        if c == 0:  # verifica se é o primeiro valor
            lista.append(num)  # e insere o novo valor a lista
            print('Este valor vai para o final da lista...')
        elif num > lista[-1]:  # verifica se é o maior valor da lista a partir do último elemento da lista
            lista.append(num)  # e insere o o novo maior valor ao final da lista
            print('Este valor vai para o final da lista...')
    #   if c == 0 or num > lista[-1]: Forma simplificada do código acima
        #   lista.append(num)
        #   print('Este valor vai para o final da lista...')
        else:
            pos = 0
            while pos < len(lista):  # enquanto a posição for menor que o tamanho da lista
                if num <= lista[pos]:  # verifica se o número inserido na pos é menor e
                    lista.insert(pos, num)  # insere o número na pos 0 caso seja o menor valor
                    print(f'Este valor foi adicionado na posição {pos} da lista...')
                    break
                pos += 1
print('-=' * 30)
print(f"Os valores digitados em ordem foram: {lista}")
