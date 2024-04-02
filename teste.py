palavra1 = ""
palavra2 = ""

while palavra1 != "sair" and palavra2 != "fim":
    palavra1 = input("Digite uma palavra ou 'sair' para terminar: ")
    palavra2 = input("Digite outra palavra ou 'fim' para terminar: ")
    print(f'Você digitou: {palavra1} e {palavra2}')
