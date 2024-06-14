# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite a expressão: '))
pilha = []
for simb in exp:  # para cada simbolo na exp:
    if simb == '(':  # se simbolo for um '(' abrindo
        pilha.append('(')  # então o programa colocará dentro da pilha
    elif simb == ')':  # se for um ")" fechando
        if len(pilha) > 0:  # e len da pilha for maior que 0
            pilha.pop()  # removerá o último elemento na pilha
        else:  # se for menor\ que zero
            pilha.append(')')  # colocará um ")" na pilha
            break
if len(pilha) == 0:  # verifica se len de pilha é igual a zero, se for,
    print('Sua expressão está correta!')  # a expressão estará correta
else:
    print('Sua expressão está errada!')  # se for maior, a expressão estará errada
