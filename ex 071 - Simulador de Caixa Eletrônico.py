num = float(input('Qual valor quer sacar? '))
cinq = num // 50
vinte = num % 50 // 20
dez = num % 50 % 20 // 10
cinco = num % 50 % 10 // 5
print(cinq, vinte, dez, cinco)
