'''
PRIM
'''
import random

def mejorNodo(candidatos, visitado):
    peso=float('inf')
    nodo= None
    for i in range(len(candidatos)):
        if candidatos[i]<peso and visitado[i]==False:
            peso= candidatos[i]
            nodo=i
    return nodo,peso

def prim(grafo):
    #tamaño y nodo inicial
    tam=len(grafo)
    nodoInicial=random.randint(0,tam-1)

    #solucion va a ser un numero
    solucion= 0

    #candidatos va a ser un vector de distancias
    candidatos=[float('inf')]*tam

    #lista de visitados para evitar repetidos
    visitado=[False]*tam

    #inicializamos el primer nodo
    visitado[nodoInicial]= True
    for inicio,fin,peso in grafo[nodoInicial]:
        candidatos[fin]=peso

    #bucle voraz
    for _ in range(1,tam):
        #elegimos el mejor
        mejor=mejorNodo(candidatos, visitado)
        solucion= solucion+mejor[1]
        visitado[mejor[0]]=True
        #vamos a actualizar
        for (inicio,fin,peso) in grafo[mejor[0]]:
            candidatos[fin]=min(candidatos[fin], peso)
    if solucion%5!=0:
        solucion=solucion//5
        solucion= solucion+1
    else:
        solucion=solucion//5
    print(solucion)


### main programa ###
primeraLinea= input().split(" ")
nodos=int(primeraLinea[0])
aristas=int(primeraLinea[1])

grafo=[]
for i in range(nodos):
    grafo.append([])

for _ in range(aristas):
    trozo=input().split(" ")
    tupla1=(int(trozo[0]), int(trozo[1]), int(trozo[2]))
    tupla2=(int(trozo[1]), int(trozo[0]), int(trozo[2]))
    grafo[int(trozo[0])].append(tupla1)
    grafo[int(trozo[1])].append(tupla2)

prim(grafo)