numero = int(input("ingrese un numero positivo de uno a cuatro digitos(1 a 9999):",))
if numero <= 9999 and numero >= 1:
    if numero < 10:
        print(numero," tiene un digito")
    elif numero < 100:
        print(numero," tiene dos digitos")
    elif numero < 1000:
        print(numero," tine tres digitos")
    elif numero < 10000:
        print(numero," tiene cuatro digitos")
print("fin")
############ 