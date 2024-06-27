capitales={}
for x in range(5):
    capital=input('ingrese una capital:')
    pais=input('ingrese el pais de la capital:')
    capitales[capital]=pais
turista=input('ingrese el nombre del turista:')
capital=input('ingrese la capital del turista:')
print(f'El turista de nombre {turista} viene de la capital {capital} y su pais es {capitales[capital]}')