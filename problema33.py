lista = ['azul', 'amarillo', 'amarillo', 'azul',
         'amarillo', 'verde', 'verde', 'rojo']

contadorVerde = 0
contadorAmarillo = 0
contadorRojo = 0
contadorAzul = 0


for i in lista:
    if i == 'azul':
       contadorAzul  += 1

    elif i == 'verde':
       contadorVerde += 1

    elif i == 'rojo':
       contadorRojo += 1

    elif i == 'amarillo':
        contadorAmarillo += 1

print(f'cantidad de color rojo: {contadorRojo}')
print(f'cantidad de color amarillo: {contadorAmarillo}')
print(f'cantidad de color verde: {contadorVerde}')
print(f'cantidad de color azul: {contadorAzul}')
print(len(lista))
