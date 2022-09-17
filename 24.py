x=0
while(x!=5):
      print(f'1. sumar \n 2. restar \n 3 multiplicar\n 4 dividiar')
      entrada = int(input('escoger opcion: '))
      if entrada == 1:
          print('ha escogido la operacion sumar')
          numeroOne=int(input('ingrese un numero: '))
          numeroTwo = int(input('ingrese un numero: '))
          sumar = numeroOne + numeroTwo
          print(f'sumar: {sumar}')
      elif entrada == 2:
          print('ha escogido la operacion restar')
          numeroOne=int(input('ingrese un numero: '))
          numeroTwo = int(input('ingrese un numero: '))
          restar = numeroOne - numeroTwo
          print(f'restar {restar}')
      elif entrada == 3:
          print('ha escogido la operacion multiplicar')
          numeroOne=int(input('ingrese un numero: '))
          numeroTwo = int(input('ingrese un numero: '))
          multi = numeroOne * numeroTwo
          print(f'restar {multi}')
      elif entrada == 4:
          print('ha escogido la operacion multiplicar')
          numeroOne=int(input('ingrese un numero: '))
          numeroTwo = int(input('ingrese un numero: '))
          dividir = numeroOne / numeroTwo
          print(f'restar {dividir}')
      elif entrada ==5:
          print('saliendo del programa...')
          break
      else:
          print('numero equivocado')
          
      
    
          