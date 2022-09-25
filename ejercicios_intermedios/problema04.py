password = input('ingrese contraseña: ')
if (len(password)>8 and 20<len(password))  and (password.isalnum() is not password.isalpha()):
    print('contraseña correcta')
else:
    print('contraseña no correcta')