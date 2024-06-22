lista=[]
while True:
    palabras=input('palabra,enter para finalizar:')
    if palabras=='':
        break
    lista.append(palabras)
for palabra in lista: 
    cont=0
    for letra in palabra:
        if letra=='a'or letra=='A':
            cont+=1
    print(palabra,'tine',cont,'as.')