lista = list()
suma=0
for i in range(5):
    entrada = int(input('ingrese valores: '))
    lista.append(entrada)
suma = lista[0]+lista[-1]
print(suma)