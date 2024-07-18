#ejemplos:
#10=2
#123456789=9
#1392037481983=13
###
def digitos(num):
    a=[]
    for x in num:
        a.append(x)
    return len(a)

###
num=input('ingrese un numero:')
print('la cantidad de digitos en el numero es:', digitos(num))

###