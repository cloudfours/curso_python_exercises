from datetime import date
year = int(input('año: '))
month= int(input('mes: '))
day = int(input('dia: '))
year1 = int(input('año: '))
month1= int(input('mes: '))
day1 = int(input('dia: '))
fecha1=date(year,month,day)
fecha2=date(year1,month1,day1)
dias = fecha2 - fecha1
print(dias.days)