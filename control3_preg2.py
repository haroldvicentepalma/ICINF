#ejemplos:
#1002013=false
#10101010=true
###
def es_binario(var):
    for x in var:
        if not x in ('1','0'):
            return False
    return True

###
var=input('ingrese un numero binario:')
#si es true imprime 'es binario'
#si es false imprime 'no es binario'
if es_binario(var)==True:
    print('es binario')
else:
    print('no es binario')

###