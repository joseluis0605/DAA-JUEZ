'''
FERNANDO SIMON ALMENDRAS
algoritmo de la mochila
'''
import copy

def mejorOpcion(copia):
    mejor= copia[0]
    copia.remove(mejor)
    return mejor
def voraz(listaOrdenada, numeroAlmendras, valorNutritivo, valorMaximoPeso):
    #solucion (indices)
    solucion=[0]*numeroAlmendras
    copia= copy.deepcopy(listaOrdenada)
    i=0
    beneficio=0

    while valorMaximoPeso>0 and copia:
        mejorSolucion= mejorOpcion(copia)
        if valorMaximoPeso-mejorSolucion[1]>=0:
            beneficio= beneficio+ mejorSolucion[0]
            valorMaximoPeso= valorMaximoPeso-mejorSolucion[1]
            solucion[i]=1
        else:
            # cogemos la proporcion
            proporcionBeneficio= (valorMaximoPeso/solucion[1])*solucion[1]
            beneficio= beneficio+proporcionBeneficio
            valorMaximoPeso=0
            solucion[i]=(solucion[1]/proporcionBeneficio)
        i= i+1

    if beneficio>=valorNutritivo and valorMaximoPeso>=0:
        print("PUEDE")
    else:
        print("TOS")


### main programa ###
primeraLinea= input().split(" ")
numeroAlmendras=int(primeraLinea[0])
numeroPruebas= int(primeraLinea[1])
vector=[]

# posicion 0= valor y posicion 1= peso
for i in range(numeroAlmendras):
    trozo=input().split(" ")
    valor=(int(trozo[0]), int(trozo[1]),int(trozo[0])/int(trozo[1]))
    vector.append(valor)

#ordenamos nuestra lista de truplas
listaOrdenada= sorted(vector, key=lambda x:-x[2])
for i in range(numeroPruebas):
    trozo = input().split(" ")
    valorNutritivo = int(trozo[0])
    valorMaximoPeso = int(trozo[1])
    voraz(listaOrdenada, numeroAlmendras, valorNutritivo, valorMaximoPeso)


'''
5 3
66 24
10 21
84 14
95 98
20 22
207 75
166 85
184 82
'''