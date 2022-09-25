entrada = None
farenheit = 0
centigrados = 0
kelvin=0
while(entrada != 4):
    print('1. convertir de grados a farethein \n 2. convertir a centigrados \n 3. convertir a kelvin \n 4. salir')
    entrada = int(input('escoja una opcion'))
    if entrada == 1:
        print('convertir a fareinheit')
        centigrados = (input('ingrese valor en grados: '))
        if centigrados.isdigit():
            farenheit = float(centigrados)* 1.8+32
            print(farenheit)
        else:
            print('no se permite letras')
    elif entrada == 2:
        print('convertir a centigrados')
        farenheit = (input('ingrese valor en grados: '))
        if farenheit.isdigit():
            centigrados = ((32*float(farenheit))-32)
            print(centigrados)
        else:
            print('error ingreso caracteres')
    elif entrada == 3:
        print('convertir a kelvin')
        farenheit = input('ingrese valor en grados: ')
        if farenheit.isdigit():
            kelvin = ((32*float(farenheit))-32)*5/9+273.15
            print(kelvin)
        else:
            print('error ingreso caracteres')
