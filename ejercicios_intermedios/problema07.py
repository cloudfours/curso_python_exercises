setencia = input('ingrese sentencia: ')
oracion = list(setencia)
for i in range(len(setencia)):
    if i% 3 == 0:
        print(oracion[i])