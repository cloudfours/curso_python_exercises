dias={'lun':'lunes','mar':'martes','mier':'miercoles','juev':'jueves','vier':'vier','sab':'sabado','dom':'domingo'}
dia = input('escriba las tres o cuatro letras del dia: ')
if dias.get(dia):
    print(dias[dia])
else:
    print('no existe')
