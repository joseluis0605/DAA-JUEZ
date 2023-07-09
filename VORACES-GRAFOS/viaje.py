'''
usamos el algoritmo de dijkstra para ver el camino mas corto de cada nodo
a cada nodo
vamos a hacer un dijkstra de todos los nodos
en donde vamos a tener que sacar la distancia maxima de todos los nodos para garantizar que con
esa distancia vamos a llegar a todos los nodos
'''

def mejor(distancias, visitado):
    nodo = None
    peso = float('inf')
    for i in range(len(distancias)):
        if not visitado[i] and distancias[i] < peso:
            peso = distancias[i]
            nodo = i
    return nodo

def dijkstra(grafo, nodo):
    #tam
    tam= len(grafo)
    visitado=[False]*tam
    distancia=[float('inf')]*tam

    visitado[nodo]=True
    for origen,fin,peso in grafo[nodo]:
        distancia[fin]= peso
    distancia[nodo]=0

    #bucle voraz
    for _ in range(1,tam):
        nextNodo= mejor(distancia, visitado)
        visitado[nextNodo]=True
        for origen,destino,peso in grafo[nextNodo]:
            distancia[destino]=min(distancia[destino], distancia[origen]+peso)
    return distancia

if __name__=='__main__':
    primeraLinea = input().split(" ")
    numeroNodos = int(primeraLinea[0])
    numeroAristas = int(primeraLinea[1])

    grafo = []
    for i in range(numeroNodos):
        grafo.append([])

    for i in range(numeroAristas):
        linea = input().split(" ")
        tupla1 = (int(linea[0]), int(linea[1]), int(linea[2]))
        tupla2 = (int(linea[1]), int(linea[0]), int(linea[2]))
        grafo[int(linea[0])].append(tupla1)
        grafo[int(linea[1])].append(tupla2)

    maximo=0
    for i in range(len(grafo)):
        distancia= dijkstra(grafo,i)
        for j in distancia:
            if maximo<j:
                maximo= j
    print(maximo)





'''
5 7
0 1 10
0 2 20
0 3 30
0 4 40
1 2 5
2 3 9
3 4 10
'''