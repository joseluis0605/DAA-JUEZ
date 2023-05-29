'''
HOSTIA PILOTES
hay que calcular el numero de componentes conexas que tiene el grafo
recorrido profundidad
'''

def numeroComponentesConexsas(grafo, numeroPilotes):
    visitado= []
    contador= 0

    for nodo in range(numeroPilotes):
        if nodo not in visitado:
            recorrido(grafo, visitado, nodo)
            contador= contador+1
    return contador

def recorrido(grafo, visitado, nodo):
    #print(nodo, end=" ")
    visitado.append(nodo)
    for nodoHijo in grafo[nodo]:
        if nodoHijo not in visitado:
            recorrido(grafo, visitado, nodoHijo)


### main programa ###
primeraLinea= input().split(" ")
numeroPilotes= int(primeraLinea[0])  # numero de nodos
numeroParesPilotes= int(primeraLinea[1]) # aristas del grafo

grafo=[]
for i in range(numeroPilotes):
    grafo.append([])



for i in range(numeroParesPilotes):
    aristas= input().split(" ")
    primera= int(aristas[0])
    segunda= int(aristas[1])
    grafo[primera].append(segunda)
    grafo[segunda].append(primera)

resultado= numeroComponentesConexsas(grafo, numeroPilotes)
print(resultado)

'''
10 5
0 1
1 5
2 4
3 9
4 9
'''

