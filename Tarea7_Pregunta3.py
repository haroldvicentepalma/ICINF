supermercado={}
while True:
    producto=input('producto,para finalizar precione enter:')
    if producto=='':
        break
    cantidad=int(input('cantidad del producto:'))
    supermercado[producto]=cantidad
x=int(input('ingrese un numero que multiplique la cantidad de los productos:'))
for y in supermercado: 
    print(y,':',supermercado[y]*x)