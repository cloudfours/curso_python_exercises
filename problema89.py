import random
lista = list()
sumo=0
for i in range(20):
    lista.append(random.randint(1,20))
    num = lista
    if lista[i]%2==0:
       par = lista
    sumo = par+num
print(sumo)


 
 