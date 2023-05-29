'''
HACKERMAN
tenemos que encontrar los puntos criticos, es decir, que si se eliminan, dividen el grafo en mas componentes conexas
'''
import copy

def programa(grafo, costeRefuerzo, tam):
    listado=[]
    size= len(grafo)
    contador=0
    for i in range(size):
        grafoAux= copy.deepcopy(grafo)
        grafoAux= eliminarNodo(grafoAux, i)
        esComponente= esComponenteConexa(grafoAux)
        if esComponente:
            listado.append(i)
    for i in listado:
        contador= contador+ int(costeRefuerzo[i])
    print(contador)

# funcion que cuenta el numero de componentes conexas
def esComponenteConexa(grafo):
    visitado=[]
    tam= len(grafo)
    contador=0
    for nodo in range(tam):
        if nodo not in visitado:
            recorrido(grafo, visitado, nodo)
            contador= contador+1

    if contador>2:
        return True
    else:
        return False
def recorrido(grafo, visitado, nodo):
    visitado.append(nodo)
    for nodoHijo in grafo[nodo]:
        if nodoHijo not in visitado:
            recorrido(grafo, visitado, nodoHijo)

# funcion que elimina el nodo y devuelve el grafo sin el nodo
def eliminarNodo(grafo, nodo):
    grafoAux= copy.deepcopy(grafo)
    grafoAux[nodo]=[]
    tam= len(grafo)
    for nodoHijo in range(tam):
        if nodo in grafoAux[nodoHijo]:
            grafoAux[nodoHijo].remove(nodo)
    return grafoAux


### main program ###
primeraLinea= input().split(" ")
nodos= int(primeraLinea[0])
conexiones= int(primeraLinea[1])

grafo=[]
for i in range(nodos):
    grafo.append([])

costeRefuerzo=[]
for i in range(nodos):
    coste= int (input())
    costeRefuerzo.append(coste)

for i in range(conexiones):
    trozo=input().split(" ")
    primer= int(trozo[0])
    segundo= int(trozo[1])
    grafo[primer].append(segundo)
    grafo[segundo].append(primer)
programa(grafo, costeRefuerzo, nodos)

'''
6 5
50
22
58
99
38
21
0 1
1 2
2 3
3 4
4 5
'''