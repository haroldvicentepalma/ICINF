def separar(lista):
    pares=[]
    impares=[]
    for x in lista:
        if x%2==0:
            pares.append(x)
            pares.sort()
        else:
            impares.append(x)
            impares.sort()
    return pares, impares
pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)
