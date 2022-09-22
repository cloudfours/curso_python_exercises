
lista =list()
for i in range(6):
    dni=int(input('ingrese su dni'))
    lista.append(dni)
lista.sort(reverse=True)
print(lista)
