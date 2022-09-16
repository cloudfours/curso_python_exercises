entrada = input('INGRESE UN CARACTER: ')
vocales = ['a', 'e', 'i', 'o', 'u']
mensaje = None
for i in vocales:

    if i == entrada:
        mensaje = True
        break
    else:
        mensaje = False


print(mensaje)
