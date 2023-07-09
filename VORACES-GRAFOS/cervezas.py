'''
algoritmo de dijkstra para el camino minimo
usaremos vector de precencia
'''
def mejorOpcion(visitados, distancias):
    nodo= None
    peso= float('inf')
    for i in range(len(distancias)):
        if not visitados[i] and distancias[i]<peso:
            peso= distancias[i]
            nodo=i
    return nodo

def dijkstra(grafo, origen, destino):
    #tamaño
    tam= len(grafo)
    #visitados para evitar volver a usar nodos repetidos
    visitados=[False]*tam
    #conjunto de distancias hacia todos los nodos
    distancias=[float('inf')]*tam
    #vector precendencia
    vectorPrecendencia=[float('inf')]*tam

    '''
    inciamos con el primero como dijkstra normal pero lo que hacermos es que vamos a ir actualizando el vector
    de precedencia tambien a medida que vamos avanzando
    '''
    visitados[origen]=True
    for inicio,fin,peso in grafo[origen]:
        distancias[fin]= peso
        vectorPrecendencia[fin]= origen

    #iniciamos el bucle voraz
    for _ in range(1, tam):
        siguiente= mejorOpcion(visitados,distancias)
        visitados[siguiente]=True
        #expandimos
        for inicio,fin,peso in grafo[siguiente]:
            if not visitados[fin]:
                oldValor= distancias[fin]
                distancias[fin]= min(distancias[fin], distancias[inicio]+peso)
                #si ha cambiado
                if oldValor!=distancias[fin]:
                    #cambiamos de donde proviene nuestro nodo
                    vectorPrecendencia[fin]= siguiente
    print(distancias[destino])

    #ahora vemos de donde procede
    encontrado= False
    camino=[]
    camino.append(destino)
    while not encontrado:
        padre= vectorPrecendencia[destino]
        if padre==origen:
            encontrado= True
        else:
            camino.insert(0,padre)
            destino= padre
    camino.insert(0, origen)

    print(*camino)



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

    distancia= input().split()
    origen=int(distancia[0])
    destino= int(distancia[1])
    dijkstra(grafo, origen, destino)