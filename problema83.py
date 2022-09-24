entrada = input('ingrese nombre:')
oracion = list(entrada)
for i in oracion:
    if i.startswith('f'):
        print(i)