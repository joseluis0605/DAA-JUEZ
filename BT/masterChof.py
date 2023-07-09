'''
algoritmo de BT usando la mochila
la solucion va a ser un vector con 1 o 0
la etapa va a ser cada una de los alimentos, cada poscion del vector lista
el intento va a ser poner 1 o 0
'''
import copy

def esFactible(lista, solucion, solucionMejor, gananciaMejor, tamMaximo, etapa, numeroAlimentos, intento, pesoAcumulado):
    miObjeto= lista[etapa]
    if intento==0:
        return True
    else:# 0 nombre 1 peso 2 valor
        if miObjeto[1]+pesoAcumulado[0]<=tamMaximo:
            return True
        else:
            return False

def BT(lista, solucion, solucionMejor, gananciaMejor, tamMaximo, etapa, numeroAlimentos, pesoAcumulado):
    intento=0
    #mientras el intento sea menor que 2
    while intento<=1:
        #es factible ponerlo a ese valor????
        if esFactible(lista, solucion, solucionMejor, gananciaMejor, tamMaximo, etapa, numeroAlimentos, intento, pesoAcumulado):
            #vemos que es factible por lo que vamos a actualizar
            solucion[etapa]= intento
            if intento==1: # 0 nombre 1 peso 2 valor
                miObejto= lista[etapa]
                gananciaMejor[0]= gananciaMejor[0]+miObejto[2]
                pesoAcumulado[0]= pesoAcumulado[0]+miObejto[1]
            #hemos llegado al final
            if etapa==len(solucion)-1:
                    if gananciaMejor[0]>gananciaMejor[1]:
                        #es mucho mejor, por lo que actualizamos
                        gananciaMejor[1]= gananciaMejor[0]
                        pesoAcumulado[1] = pesoAcumulado[0]
                        solucionMejor= copy.deepcopy(solucion)
            else:
                BT(lista, solucion, solucionMejor, gananciaMejor, tamMaximo, etapa+1, numeroAlimentos, pesoAcumulado)
            if intento==1: #0 nombre 1 peso 2 valor
                miObejto = lista[etapa]
                gananciaMejor[0] = gananciaMejor[0] - miObejto[2]
                pesoAcumulado[0] = pesoAcumulado[0] - miObejto[1]
                solucion[etapa]=0
        intento= intento+1



### main program ###
primeraLinea= input().split(" ")
numeroAlimentos=int(primeraLinea[0])
tamMaximo=int(primeraLinea[1])

lista=[]
for i in range(numeroAlimentos):
    linea= input().split(" ")
    lista.append(([linea[0]], int(linea[1]), int(linea[2])))

gananciaMejor=[0,0]
pesoAcumulado=[0,0]
solucionMejor=['-']*numeroAlimentos
solucion=['-']*numeroAlimentos

BT(lista, solucion, solucionMejor, gananciaMejor, tamMaximo, 0, numeroAlimentos,pesoAcumulado)
print(gananciaMejor[1])

'''
5 10
Perdiz 5 20
Esparragos 3 15
Aceite 2 5
Gambas 6 13
Leon 0 10
'''
