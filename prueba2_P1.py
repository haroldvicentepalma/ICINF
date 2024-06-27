notas=[]
while True:
    nota=float(input('ingrese la nota: para finalizar ingrese 0:'))
    if nota==0:
        break
    notas.append(nota)
promedio_notas=0
for x in notas:
    promedio_notas+=x
cont_m40=0
cont_M40=0
for y in notas:
    if y<4.0:
        cont_m40+=1
    elif y>=4.0:
        cont_M40+=1
print(f'1)cantidad de notas: {len(notas)}\f2)promedio de notas: {promedio_notas/len(notas)}\f3)cantidad de notas bajo 4.0: {cont_m40}\f4)cantidad de notas igual o mayor a 4.0: {cont_M40}')
