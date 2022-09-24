lista=list()

for i in range(4):
    notas = int(input('ingrese notas:'))
    lista.append(notas)

ordenado = lista.sort(reverse=True)
print(str(ordenado))
    