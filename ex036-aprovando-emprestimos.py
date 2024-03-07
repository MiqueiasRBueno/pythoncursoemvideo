# Crie um programa para aprovar o empréstimo de uma casa. O programa vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo se que não pode exceder a 30% do salário ou então o empréstimo será
# negado.

vlcasa = float(input('Qual o valor da casa a ser financiada? R$ '))
vlsal = float(input('Qual valor do seu salário? R$ '))
qtanos = float(input('Em quantos anos pretende pagar? '))
nparc = (qtanos * 12)
parc = (vlcasa / nparc)
percent = (vlsal * 30)/100
print(f'O valor da casa é de R$ {vlcasa:.2f}\nE o período escolhido é de {qtanos:.0f} anos.'
      f'\nSeu salário é de R$ {vlsal:.2f}\nO valor das parcelas são R$ {parc:.2f}')
if parc <= percent:
    print('Meus parabéns! Seu empréstimo foi aprovado!')
elif parc > percent:
    print('O valor das parcelas ultrapassaram o limite de 30% do seu salário.\nSinto muito, seu empréstimo foi negado!')
