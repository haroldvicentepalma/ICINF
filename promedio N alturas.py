flag = 1
suma = 0
cont = 0
promedioAltura = 0
while flag == 1:
    altura = float(input("ingrese la altura en metros,(ejemplo:1.75), para terminar ingrese 0: ",))
    if altura == 0:
        break
    suma = suma + altura
    cont = cont + 1
    promedioAltura =suma / cont
print("el promedio de altura es: ",promedioAltura,"m")
print("fin")
######