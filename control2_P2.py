lista_nombres=[]
for x in range(0,7):
    nombres=input("ingrese un nombre:",)
    lista_nombres.append(nombres)
for nombre in lista_nombres:
    tamaño=len(nombre)
    cont=0
    for letras in nombre:
        cont=cont+1
        if tamaño==cont:
            if letras=="a":
                lista_nombres.remove(nombre)
print(lista_nombres)