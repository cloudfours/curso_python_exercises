rango = float(input('ingrese rango de notas: '))
x=0
sum = 0
avg = 0
while(x<rango):
    x+=1
    notas=float(input('Ingrese notas: '))
    sum = sum+notas;
    avg =sum/rango
   
print(f'suma total: {sum}. media: {avg}')