lista=[]

for i  in range(1,5):
        entrada=int(input('ingrese valores'))
        lista.append(entrada)
        print(lista)

def listar(lista):
    multi=1
    sum=0
    for i in lista:
        sum +=i
        multi *=i
    print(f'suma: {sum} y multi: {multi}')


listar(lista)
        
    