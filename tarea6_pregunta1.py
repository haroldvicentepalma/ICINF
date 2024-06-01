lista=[]
palabra=input("ingrese una palabra(para finalizar deje vacio y presione enter):")
while palabra!='':
    lista.append(palabra)
    palabra=input("ingrese una palabra(para finalizar deje vacio y presione enter):")
print(lista)
cont_vocales=0
cont_consonates=0
for palabras in lista:    
    for letras in palabras:
        if letras=="a" or letras=="e" or letras=="i" or letras=="o" or letras=="u":
            cont_vocales=cont_vocales+1
        else:
            cont_consonates=cont_consonates+1
    print(palabras)
    print("vocales:",cont_vocales,"/","consonantes:",cont_consonates)
    cont_vocales=0
    cont_consonates=0
