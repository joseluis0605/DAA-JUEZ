'''
ALGORITMO DE KRUSKAL---> buscar el coste minimo para llegar a todos los nodos
'''
import random

def ordenar(grafo):
    lista=[]
    for i in grafo:
        for arista in i:
            lista.append(arista)
    lista= sorted(lista, key=lambda x:x[2])
    return lista
def prim(grafo, tipo):
    #tamaño
    tam= len(grafo)
    #candidatos son las aristas que tenemos ordenadas
    candidatosOrdenados= ordenar(grafo)
    #solucion va a ser un array con los tipos que hay
    solucion=[]
    for tipoActual in tipo:
        if tipoActual not in solucion:
            solucion.append(tipoActual)
    for i in range(len(solucion)):
        solucion[i]=float('inf')

    print(tipo)
    #bucle voraz
    while candidatosOrdenados:
        (origen,fin,peso)= candidatosOrdenados[0]
        candidatosOrdenados.remove(candidatosOrdenados[0])
        #si son del mismo tipo
        tipoOrigen=int(tipo[origen])
        tipoDestino = int(tipo[fin])
        if tipoOrigen==tipoDestino:
            if solucion[tipoOrigen]>peso:
                solucion[tipoOrigen]=peso
    print(*solucion)



if __name__=='__main__':
    primeraLinea=input().split(" ")
    nodos=int(primeraLinea[0])
    aristas=int(primeraLinea[1])

    grafo=[]
    for i in range(nodos):
        grafo.append([])

    tipo=(input().split(" "))

    for i in range(aristas):
        trozo=input().split(" ")
        tupla1=(int(trozo[0]),int(trozo[1]) ,int(trozo[2]))
        tupla2=(int(trozo[1]),int(trozo[0]), int(trozo[2]))
        grafo[int(trozo[0])].append(tupla1)
        grafo[int(trozo[1])].append(tupla2)

    prim(grafo, tipo)

'''
6 10
0 0 0 1 1 1
0 1 2
0 3 1
0 2 5
1 2 3
1 3 2
2 3 3
2 4 1
2 5 5
3 4 1
4 5 1
'''