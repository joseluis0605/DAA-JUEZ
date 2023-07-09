'''
algoritmo que colorea grafos en BT
la solucion va a ser un array en donde la posicion es el nodo y el contenido el id del examen
la etapa va a ser cada una de los alumnos (posiciones del vector)
el intento va a ser asignarle un examen u otro
'''
def esFactible(solucion,etapa,numeroColores,intento, matriz):
    #vamos a ver si algunos de los adyacentes de mi amigo son iguales a intento
    for i in range(len(solucion)):
        if matriz[etapa][i]==True and intento==solucion[i]:
            return False
    return True

def BT(solucion,etapa, numeroColores, matriz):
    exito=False
    intento=0
    while intento<numeroColores and not exito:
        #es factible marcar a este alumno (etapa) con este id de examen (intento)
        if esFactible(solucion,etapa,numeroColores,intento, matriz):
            #es factible, por lo que vamos a marcar cojones
            solucion[etapa]= intento
            if etapa==len(solucion)-1:
                #hemos llegado a la  final por fin
                exito= True
            else:
                #seguimos bajando tu, como el betis
                exito= BT(solucion, etapa+1, numeroColores, matriz)
            if not exito:
                #somos unos desgraciados, exito es falso, asi que vamos subiendo y desmarcamos
                solucion[etapa]=False
        intento= intento+1
    return exito


# main program #
primeraLinea= input().split(" ")
numeroNodos= int(primeraLinea[0])
numeroAristas= int(primeraLinea[1])

matriz=[]
for i in range(numeroNodos):
    fila= [False]*numeroNodos
    matriz.append(fila)

for i in range(numeroAristas):
    arista= input().split(" ")
    alumno1= int(arista[0])
    alumno2= int(arista[1])
    matriz[alumno1][alumno2]=True
    matriz[alumno2][alumno1]=True

solucion=[-1]*numeroNodos

exito=False
numeroColores=2
while not exito:
    exito= BT(solucion,0, numeroColores, matriz)
    if not exito:
        numeroColores= numeroColores+1
if exito:
    print(numeroColores)


'''
5 7
0 1
0 2
0 3
0 4
1 2
2 3
3 4
'''