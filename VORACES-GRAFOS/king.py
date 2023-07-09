'''
'''
def mejorOpcion(visitados, distancias):
    nodo= None
    peso= float('inf')
    for i in range(len(distancias)):
        if not visitados[i] and distancias[i]<peso:
            peso= distancias[i]
            nodo=i
    return nodo,peso

def prim(grafo, nodoInicio):
    #tamaño
    tam= len(grafo)

    #solucion va a ser un numero
    solucion=0

    #vector distancias para comparar las distancias
    distancias=[float('inf')]*tam

    #visitados para no volver atras
    visitados=[False]*tam

    #inciamos el primer nodo
    visitados[nodoInicio]=True
    for origen,destino,peso in grafo[nodoInicio]:
        distancias[destino]= peso

    #bucle voraz
    for _ in range(1,tam):
        (fin,peso)= mejorOpcion(visitados, distancias)
        solucion= solucion+peso
        visitados[fin]=True
        #actualizamos
        for origen,destino, peso in grafo[fin]:
            if not visitados[destino]:
                distancias[destino]= min(distancias[destino], peso)
    print(solucion)


if __name__=='__main__':
    primeraLinea=input().split(" ")
    numeroNodos= int(primeraLinea[0])
    numeroAristas= int(primeraLinea[1])

    grafo=[]
    for i in range(numeroNodos):
        grafo.append([])

    for i in range(numeroAristas):
        linea=input().split(" ")
        tupla1= (int(linea[0]), int(linea[1]), int(linea[2]))
        tupla2 = (int(linea[1]), int(linea[0]), int(linea[2]))
        grafo[int(linea[0])].append(tupla1)
        grafo[int(linea[1])].append(tupla2)

    prim(grafo, 0)