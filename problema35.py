listaNombre=[]
for i in range(5):
    nombres = input('ingrese nombres: ')
    listaNombre.append(nombres)
    listaNombre.sort(reverse=True)
    print(listaNombre)