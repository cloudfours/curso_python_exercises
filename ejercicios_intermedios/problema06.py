number= int(input('ingrese el valor: '))
def table(numb):
    for i in range(1,10):
        mul = numb*i
        print(f'{numb}x{i}={mul}')
        
table(number)