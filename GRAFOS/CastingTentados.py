'''
CASTING TENTADOR
consiste en saber si solo es una unica componente conexa
recorrido en profundidad
'''
from collections import deque


def profundidad(grafo):
    nodoToca=0
    valida= True
    while nodoToca<len(grafo) and valida:
        numero=componentesConexas(grafo, nodoToca)
        if numero==True:
            valida=False
        else:
            nodoToca= nodoToca+1

    if valida==False:
        print("HAY QUE REPETIR")
    else:
        print("CASTING COMPLETO")

def componentesConexas(grafo, nodoToca):
    tam= len(grafo)
    visitado= []
    contador=0
    i= 0
    max= len(grafo)
    while i<max:
        if nodoToca not in visitado:
            recorrido(grafo, nodoToca, visitado)
            contador= contador+1
        if contador>1:
            return True
        else:
            i= i+1
            nodoToca= nodoToca+1
            if nodoToca==max:
                nodoToca=0
    return False

def recorrido(grafo, nodoToca, visitado):
    visitado.append(nodoToca)
    cola=deque()
    cola.append(nodoToca)
    while cola:
        nodoHijo= cola.popleft()
        for nodo in grafo[nodoHijo]:
            if nodo not in visitado:
                cola.append(nodo)
                visitado.append(nodo)


### main programa ###

primeraLinea= input().split(" ")
numeroNodos= int(primeraLinea[0])
numeroAristas=int(primeraLinea[1])

grafo=[]
for i in range(numeroNodos):
    grafo.append([])

for i in range(numeroAristas):
    trozo=input().split(" ")
    primer=int(trozo[0])
    segundo= int(trozo[1])
    grafo[primer].append(segundo)

profundidad(grafo)