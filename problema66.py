def tomar_valore():
    lista = []
    for i in range(3):
        valores = int(input('ingrese valores: '))
        lista.append(valores)
    return lista


def media(lista):
    return len(lista)


def calcular_total(lista):
    sum = 0
    avg = 0
    for i in lista:
        sum += i
    avg = sum/media(lista)
    return f'suma: {sum} media: {avg}'


def mostrar(funcion):
    return funcion

print(mostrar(calcular_total(tomar_valore())))
