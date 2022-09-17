entrada = int(input('ingrese nota'))

if entrada:
    if entrada >= 60 and entrada <= 70:
        print(f'su nota es C')
    elif entrada >= 80 and entrada <= 90:
        print(f'su nota es B or A')
    elif entrada >= 95:
        print('su nota es +A')
    elif entrada <=60:
        print('su nota es D')
else:
    print('ingrese valores numericos')