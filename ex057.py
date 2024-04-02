gen = str(input('Informe seu sexo [ F/ M]: ')).upper()
gen2 = ''
while gen != "F" and gen != "M":

    if gen != 'F' and gen != 'M':
        gen2 = str(input('Dados incorretos! Por favor, informe seu sexo [ F / M ]: ')).upper()
        if gen2 == 'F' and gen2 == 'M':
            print('Sexo {} registrado com sucesso!'.format(gen2))
        else:
            print('Sexo {} registrado com sucesso!'.format(gen2))
print('Sexo {} registrado com sucesso!'.format(gen))
