totalP = int(input("Ingrese el numero total de preguntas: ", ))
respuestasC = int(input("Ingrese el numero de respuestas correctas: ", ))
Porcentaje = (respuestasC * 100) / totalP
if Porcentaje >= 95:
    print(Porcentaje,"%","Nivel máximo")
elif Porcentaje >= 70 and Porcentaje < 95:
    print(Porcentaje,"%","Nivel medio")
elif Porcentaje >= 40 and Porcentaje < 70:
    print(Porcentaje,"%","Nivel regular")
elif Porcentaje < 40:
    print(Porcentaje,"%","Fuera de nivel")
