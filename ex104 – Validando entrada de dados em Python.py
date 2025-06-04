# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# Função
def leiaInt(msg):
    ok = False # variável ok enquanto falso, programa entra em loop
    valor = 0 # Adiciona um valor 0 a variável valor
    while True: # Loop infinito
        num = str(input(msg)) # recebe mensagem de n
        if num.isnumeric(): # verifica se a variável num é um valor numérico
            valor = num # se 'n' for numérico, valor recebe 'n'
            ok = True # ok passa ser verdadeiro quando valor recebe um valor numérico
        else: # se num for um valor diferente de numérico
            print('\033[0;31mERRO! Digite um valor numérico válido!\033[m') # Mensagem de erro para valores diferentes
            # de numérico
        if ok: # Se ok for verdadeiro
            break # termina o programa
    return valor


# programa principal
n = leiaInt('Digite um valor: ') # Adiciona um valor a função como input
print(f'Você digitou o valor {n}.') # exibe uma mensagem com o valor
