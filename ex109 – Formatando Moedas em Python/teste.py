# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# Importação de módulo:
import moeda

# Programa principal:
preco = float(input('Digite o preço: R$ '))
print(f'Aumentando 10 % de {moeda.moeda(preco)} temos {moeda.aumentar(preco, 10, True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'O preço de {moeda.moeda(preco)} menos 15 % é de {moeda.diminuir(preco, 15, True)}')
