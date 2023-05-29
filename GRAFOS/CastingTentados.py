'''
CASTING TENTADOR
consiste en saber si solo es una unica componente conexa
recorrido en profundidad
'''

def profundidad(grafo):
    tam= len(grafo)
    visitado=[]
    contador=0
    for i in range(tam):
        if i not in visitado:
            recorrido(grafo, visitado, i)
            contador= contador+1
    if contador==1:
        print("CASTING COMPLETO")
    else:
        print("HAY QUE REPETIR")
def recorrido(grafo, visitado, nodo):
    visitado.append(nodo)
    for nodoHijo in grafo[nodo]:
        if nodoHijo not in visitado:
            recorrido(grafo, visitado, nodoHijo)


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