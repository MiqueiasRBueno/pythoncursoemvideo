# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

# Importação de módulo:
import moeda

# Programa principal:
preco = float(input('Digite o preço: R$ '))
print(f'Aumentando 10 % de {moeda.moeda(preco)} temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'O preço de {moeda.moeda(preco)} menos 15 % é de {moeda.moeda(moeda.diminuir(preco, 15))}')
