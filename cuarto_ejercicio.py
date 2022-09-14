edad = int(input('ingrese edad: '))

if edad <= 10:
    print('no puede participar')
else:
    if edad > 18:
        print('puede particiar')
    else:
        print('no puede votar a un.')
