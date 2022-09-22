import os
entrada = int(input('Escoja una opcion: '))
while(entrada!=4):
    print('1. crear archivo, 2.ingresar informacion, 3.mostrar la informacion,4.cerrar')
    if entrada == 1:
        ingresar = input('ingrese nombre del archivo: ')
        archivo=open(ingresar+'.txt','x')
        if os.path.exists(ingresar):
             raise FileExistsError(0,'ya existe')
        else:
             print('se creado con exito')
    elif entrada==2:
        ingresar = input('ingrese nombre del archivo: ')
        archivo=open(ingresar+'.txt','a')
        nombre=input('ingrese su nombre: ')
        edad=int(input('ingrese su edad: '))
        archivo.write(nombre)
        archivo.write(str(edad))
        archivo.close()
    elif entrada==3:
        ingresar = input('ingrese nombre del archivo: ')
        archivo=open(ingresar+'.txt','r')
        print(archivo.readline())
        
