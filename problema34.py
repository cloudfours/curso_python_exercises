listaColores = []
entrada=0
while(entrada != 5):
    print('1. ingrese para agregar elementos \n 2. para eliminar el ultimo elemento \n3. mostrar elementos\n 4. Digite 5 para salir')
    entrada = int(input( 'Escojer opcion: '))   
    if entrada == 1:
        for i in range(5):
            colores = input('ingrese colores: ')
            listaColores.append(colores)
            print(listaColores)
    elif entrada == 2:
        listaColores.pop()
        print(listaColores)
    elif entrada == 3:
        print(f'colores: {listaColores}')
