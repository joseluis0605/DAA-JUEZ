'''
en este problema hay que calcular el coste minimo para llegar a todos los puntos,
para ello, vamos a usar prim o kruskal
'''
import random

'''
ALGORITMO KRUSKAL
'''

def ordenarLista(grafo):
    lista= []
    for listado in grafo:
        for arista in listado:
            lista.append(arista)
    lista= sorted(lista, key=lambda x:x[2])
    return lista

def actualizarComponente(componentesConexas, viejo, nuevo):
    for i in range(len(componentesConexas)):
        if componentesConexas[i]==viejo:
            componentesConexas[i]=nuevo
    return componentesConexas
def kruskal(grafo):
    #tamaño
    tam=len(grafo)
    #solucion es un numero
    resultado=0
    #candidatos va a ser una lista ordenada de aristas por peso
    candidatos=ordenarLista(grafo)
    #componentes para tener controlados los visitados
    componentesConexas=[]
    for i in range(tam):
        componentesConexas.append(i)
    numeroComponentes=tam-1

    while numeroComponentes>1 and candidatos:
        #mejor opcion
        (origen,destino,peso)=candidatos[0]
        candidatos.remove(candidatos[0])
        #es factible, es decir, pertence a la componente conexa o no
        if componentesConexas[origen]!=componentesConexas[destino]:
            resultado= resultado+peso
            componentesConexas= actualizarComponente(componentesConexas, componentesConexas[origen], componentesConexas[destino])
            numeroComponentes= numeroComponentes-1
    print(componentesConexas)
    print(resultado)
#main program#

primeraLinea= input().split(" ")
nodo= int(primeraLinea[0])
aristas=int(primeraLinea[1])

grafo=[]
for i in range(nodo):
    grafo.append([])

for i in range(aristas):
    trozo=input().split(" ")
    tupla1=(int(trozo[0]), int(trozo[1]), int(trozo[2]))
    tupla2=(int(trozo[1]), int(trozo[0]), int(trozo[2]))
    grafo[int(trozo[0])].append(tupla1)
    grafo[int(trozo[1])].append(tupla2)

kruskal(grafo)


'''
10 19
0 4 517
0 9 600
1 7 105
1 8 956
2 4 231
2 8 250
2 9 182
3 4 569
3 8 352
4 5 868
4 7 578
4 9 116
5 6 785
5 7 563
5 9 492
6 9 609
7 8 217
7 9 161
8 9 880
'''