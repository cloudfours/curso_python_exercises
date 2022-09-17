numeroOne=int(input('ingrese el primer numero: '))
numeroTwo = int(input('ingrese el segundo numero:'))

def NumeroMaximo(numeroOne, numeroTwo):
    if numeroOne > numeroTwo:
        print(numeroOne)
    elif numeroTwo > numeroOne:
        print(numeroTwo)
    elif numeroOne == numeroTwo:
        print('ambos son iguales')
    else:
        print('error')
        
        
NumeroMaximo(numeroOne, numeroTwo)