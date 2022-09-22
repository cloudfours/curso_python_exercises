def calcular_beca (valor):
    if valor.isdigit()==True:
        if valor <=600:
            print(f'su beca no es posible por puntaje {valor}')
        elif valor >=700:
            print(f'tendra un descuento por el 30% {valor}')
        elif valor >=800:
            print(f'tendra un descuento por el 40% {valor}')
        elif valor >=900:
            print(f'tendra un descuento por el 60% {valor}')
        elif valor >=1000:
            print(f'tendra un descuento por el 80% {valor}')
        elif valor >=1100:
            print(f'tendra un descuento por el gratis {valor}')
        else:
            print('valor no valido')
    else:
        print('ingreso cadena')
          
          
nota = int(input('ingrese valor: '))         
calcular_beca(nota)
    