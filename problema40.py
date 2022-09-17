nombre = input('ingrese su nombre: ')
def check(name):
    if name.isalnum():
        print(name)
    else:
        print('no valido')
        
check(nombre)