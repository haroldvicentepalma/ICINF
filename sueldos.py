n = 0
cont = 0
cont2 = 0
gastoT = 0
while n == 0:
    sueldos = int(input("ingrese el suldo, para finalizar ingrese -1:",))
    if sueldos == -1:
        break
    if sueldos >= 500000 and sueldos <= 900000:
        cont = cont + 1
    elif sueldos > 900000:
        cont2 = cont2 + 1
    gastoT = gastoT + sueldos
print(cont,"cobran entre 500.000 y 900.000 y",cont2,"cobran mas de 900.000")
print("la empresa gasta",gastoT,"en los sueldos del personal")
