
lista = []

for i in range(5):
    sum = 0
    datos = int(input('ingrese valores'))
    lista.append(datos)
    for i in lista:
        sum = sum+i
print(f'sumatoria de todos los elementos: {sum}')
