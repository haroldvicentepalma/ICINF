precios_CLP=[]
for x in range(10):
    precio=int(input('ingrese el precio del producto en CLP:'))
    precios_CLP.append(precio)
for y in range(10):
    precios_CLP.append(precios_CLP[y]*950)
for a in range(10):
    precios_CLP.pop(0)
print(precios_CLP)
