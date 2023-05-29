'''
MASTER CHOF
algoritmos voraces
'''
import copy

def mejorOpcion(copiaLista):
    max= copiaLista[0]
    copiaLista.remove(max)
    return max

def voraz(listaOrdenada, numeroAlimentos, tamCesta):
    #solucion
    solucion=[]

    pesoActual=0
    copiaLista= copy.deepcopy(listaOrdenada)
    beneficio=0

    while copiaLista and pesoActual<tamCesta:
        mejor= mejorOpcion(copiaLista)
        #funcion factible
        if pesoActual+mejor[1]<=tamCesta:
            beneficio= beneficio+mejor[2]
            pesoActual= pesoActual+mejor[1]
            solucion.append(mejor)
        else:
            pesoRestante= tamCesta-pesoActual
            proporcion=(pesoRestante/mejor[1])*mejor[2]
            beneficio= beneficio+proporcion
            solucion.append(mejor)
    print(beneficio)

### main programa ###
primeraLinea=input().split(" ")
numeroAlimentos= int(primeraLinea[0])
tamCesta= int(primeraLinea[1])

# 1 es tamaño y 2 es valor
lista=[]
for i in range(numeroAlimentos):
    traza=input().split(" ")
    alimento=(traza[0], int(traza[1]), int(traza[2]),int(traza[2])/int(traza[1]))
    lista.append(alimento)

listaOrdenada= sorted(lista, key=lambda x:-x[3])
voraz(listaOrdenada, numeroAlimentos, tamCesta)

'''
5 10
Perdiz 5 20
Esparragos 3 15
Aceite 2 5
Gambas 6 13
Leon 5 10
'''