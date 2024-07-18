#ejemplos:
#4**2=16
#3**3=27
#90**3=729,000
###
def potencia(num, exp):
    if exp == 1:
        return num
    else:
        return num * potencia(num, exp-1)

###
print(potencia(4,2))
print(potencia(3,3))
print(potencia(90,3))

###