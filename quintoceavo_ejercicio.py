list = []
opcion=0
while(opcion != 6):
    opcion+=1
    print('1. agregar productos: \n', 
          '2. mostrar lista de productos:  \n',
          '3. eliminar items de la lista')
    opcion = int(input('Escoja una opcion: '))
    if opcion == 1:
       for i in range(5):
            entrada = int(input('ingrese valores'))
            list.append(entrada)
            if i == 6:
                break;   
    elif opcion == 2:
        print(list)
    elif opcion == 3:
        list.clear()
        print(list)
