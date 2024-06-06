lista_puntages=[]
lista=[]
lista2=[]
cont=0
for x in range(0,15):
    puntages=int(input("ingrese el puntage del dia:",))
    lista_puntages.append(puntages)
for y in lista_puntages:
    if y<70:
        cont=cont+1
        d="dia",cont
        lista.append(d)
    elif y>=70:
        cont=cont+1
        d2="dia",cont
        lista2.append(d2)
for z in lista:
    print(z)
for z1 in lista2:
    print(z1)