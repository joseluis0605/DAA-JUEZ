'''
CORRUPCION
consiste en encontrar un bucle
recorrido en profundidad
'''

def detectorCiclo(grafo, tam):
    visitado=[]
    for nodo in range(tam):
        if nodo not in visitado:
            resultado= recorrido(grafo, visitado, nodo, nodo)
            if resultado:
                return True
    return False

def recorrido(grafo, visitado, nodo, anterior):
    visitado.append(nodo)
    for nodoHijo in grafo[nodo]:
        if nodoHijo not in visitado:
            resultado= recorrido(grafo, visitado, nodoHijo, nodo)
        elif anterior!=nodoHijo:
            return True
    return False

### main programa ###
primeraLinea= input().split(" ")
numeroNodos= int(primeraLinea[0])
numeroAristas= int(primeraLinea[1])

grafo=[]
for i in range(numeroNodos):
    grafo.append([])

for i in range(numeroAristas):
    trozo= input().split(" ")
    primer= int(trozo[0])
    segundo= int(trozo[1])
    grafo[primer].append(segundo)
    grafo[segundo].append(primer)

valor= detectorCiclo(grafo, numeroNodos)

if valor:
    print("CORRUPTOS")
else:
    print("INOCENTES")

'''
5 5
1 0
1 2
2 0
0 3
3 4
'''
'''
3 2
0 1
1 2
'''