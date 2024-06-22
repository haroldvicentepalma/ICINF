deudores={}
for x in range(5):
    rut=input('ingrese el rut de la persona:')
    deuda=int(input('ingrese la deuda de la persona:'))
    deudores[rut]=deuda
while True:
    rut=input('para pagar la deuda, ingrese el rut del deudor:')
    if rut=='':
        break
    print('deuda:',deudores[rut])
    abono=int(input('ingrese el monto del abono a la deuda:'))
    deuda=deudores[rut]-abono
    deudores[rut]=deuda
    if deuda==0:
        del(deudores[rut])
        print('deuda pagada')
print(deudores)