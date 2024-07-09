def sumatoria(numero):
    if numero==1:
        return 1
    else:
        return numero+sumatoria(numero-1)
print(sumatoria(1))
print(sumatoria(2))
print(sumatoria(3))
print(sumatoria(4))
print(sumatoria(5))