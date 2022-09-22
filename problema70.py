lista =[]
multi=0
suma=0
for i in range(3):
    num = int(input('ingrese tres valores: '))
    lista.append(num)
multi=lista[0]*lista[2]
suma = multi+lista[1]
print(suma)
    