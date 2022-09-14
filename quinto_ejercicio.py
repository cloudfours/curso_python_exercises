print('Escoja que operacion quiere acceder')
x=0
while(x<10):
    x+=1
    print('1. Sumar'
        ,'2. Restar'
        ,'3. Multiplicar'
        ,'4. Dividir'
        ,'5. Salir')
    
    entrada = int(input('Ingrese una opcion: '))
    
    if entrada ==1:
        numeroOne = float(input('Ingrese valor: '))
        numeroTwo = float(input('Ingrese valor: '))
        sum = numeroOne + numeroTwo
        print(f'su suma es: {sum}')
    elif entrada == 2:
        numeroOne = float(input('Ingrese valor: '))
        numeroTwo = float(input('Ingrese valor: '))
        restar = numeroOne - numeroTwo
        print(f'su resta es: {restar}')
    elif entrada == 3:
        numeroOne = float(input('Ingrese valor: '))
        numeroTwo = float(input('Ingrese valor: '))
        mul = numeroOne * numeroTwo
        print(f'su multiplicacion es: {mul}')
    elif entrada ==4:
        numeroOne = float(input('Ingrese valor: '))
        numeroTwo = float(input('Ingrese valor: '))
        div = numeroOne / numeroTwo
        print(f'su suma es: {sum}')
    elif entrada == 5:
        print('ha salido del programa')
        break
        
        
