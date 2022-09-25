import os
path = input('ingrese archvo con extension ')
root,extension = os.path.splitext(path)
print(f'root: {root} extension {extension}')