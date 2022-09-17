import math
angulo = float(input('ingrese valor del angulo'))
sin = math.sin(angulo)
cos = math.cos(angulo)
convertSin = math.degrees(sin)
convertCos = math.degrees(cos)
print(f'seno: {sin} coseno: {cos} convertiendo a grados seno: {convertSin} convirtiendo a grados coseno: {convertCos}')
