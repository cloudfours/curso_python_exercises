entrada_datos = int(input('Ingrese cantidad de datos'))
sum=0
avg=0
for i in range(1,entrada_datos):
    datos=int(input('ingrese datos: '))
    sum+=datos
    avg=sum/entrada_datos
    print(avg)
    