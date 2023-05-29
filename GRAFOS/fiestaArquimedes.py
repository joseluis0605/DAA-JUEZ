'''
LA FIESTA DE ARQUIMEDES
contador de componentes conexas, y mostrar las diferentes
usamos recorrido en profundidad
'''

def profundidad(grafo):
    visitado=[]
    tam= len(grafo)
    for nodo in range(tam):
        listado=[]
        if nodo not in visitado:
            recorrido(grafo, visitado, nodo, listado)
            print(*listado)

def recorrido(grafo, visitado, nodo, listado):
    visitado.append(nodo)
    listado.append(nodo)
    for nodoHijo in grafo[nodo]:
        if nodoHijo not in visitado:
            recorrido(grafo, visitado, nodoHijo, listado)


### main program ###

primeraLinea= input().split(" ")
numeroNodos= int(primeraLinea[0])
numeroAristas= int(primeraLinea[1])

grafo=[]
for i in range(numeroNodos):
    grafo.append([])

for i in range(numeroAristas):
    trozo= input().split(" ")
    primero=int(trozo[0])
    segundo=int(trozo[1])
    grafo[primero].append(segundo)
    grafo[segundo].append(primero)
profundidad(grafo)

'''
6 5
0 1
1 2
1 3
3 0
4 5
'''