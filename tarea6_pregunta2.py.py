#programa que muestre un menu con opciones para una lista
lista=[]
cont=-1
while True:
    print("1-Ingrese un elemento a la lista.")
    print("2-Modificar un elemento de la lista segun el indice.")
    print("3-Eliminar un elemento de la lista segun el indice.")
    print("4-Eliminar el ultimo elemento de la lista.")
    print("5-Buscar un elemento de la lista segun el dato(devuelve el indice).")
    print("6-Mostrar todos los elementos de la lista.")
    print("0-Salir(salir del bucle principal y finalizar).")
    opcion=int(input("accion a realizar: ",))
    if opcion==1:
        agregar=input("elemento que se va a agregar a la lista: ",)
        lista.append(agregar)
    elif opcion==2:
        modificar_eliminar=int(input("el elemento de la lista que va a ser modificado segun su indice: "))
        modificar=input("el nuevo elemento en la lista: ")
        lista.pop(modificar_eliminar)
        lista.insert(modificar_eliminar,modificar)
    elif opcion==3:
        eliminar=int(input("el elemento que va a ser eliminado segun su indice: "))
        lista.pop(eliminar)
    elif opcion==4:
        lista.pop(-1)
    elif opcion==5:
        elemento=input("el elemento que busca: ")
        for x in lista:
            cont=cont+1
            if x==elemento:
                print("el indice es: ",cont)
    elif opcion==6:
        print(lista)
    if opcion==0:
        break