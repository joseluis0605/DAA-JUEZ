'''
EXPLODING KITTENS
algoritmos voraces
'''
def mejor(listaOrdenada):
    max= listaOrdenada[0]
    listaOrdenada.remove(max)
    return max
def voraz(listaOrdenada, numeroCartas, riesgoTotal):
    #solucion
    solucion=[]
    riesgoActual=0


    while listaOrdenada and riesgoActual<riesgoTotal:
        mejorOpcion= mejor(listaOrdenada)
        #funcion factible
        if riesgoActual+mejorOpcion[1]<=riesgoTotal:
            solucion.append(mejorOpcion[0])
            riesgoActual= riesgoActual+mejorOpcion[1]
        else:
            sobrante= riesgoTotal-riesgoActual
            proporcion=(sobrante /mejorOpcion[1])*mejorOpcion[2]
            solucion.append(mejorOpcion[0])
            riesgoActual= riesgoTotal
    print(*solucion)


### MAIN PROGRAM ###
primeraLinea= input().split(" ")
numeroCartas= int(primeraLinea[0])
riesgoMaximo= int(primeraLinea[1])

# 0-> nombre 1-> riesgo 2-> beneficio 3-> beneficio/riesgo
listado=[]
for i in range(numeroCartas):
    trozo= input().split(" ")
    tupla=(trozo[0], int(trozo[1]), int(trozo[2]),int(trozo[2])/int(trozo[1]))
    listado.append(tupla)

listaOrdenada= sorted(listado, key= lambda x: -x[3])
voraz(listaOrdenada, numeroCartas, riesgoMaximo)

'''
8 150
Desactivar 1 100
VerElFuturo 10 90
HazmeUnFavor 75 50
PasaTurno 80 75
CambiaDireccion 60 25
VaASerQueNo 50 95
Barajar 40 30
Ataque 30 80
'''