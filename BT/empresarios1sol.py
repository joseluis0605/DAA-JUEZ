'''
dos empresarios quieren repartir activos por iguales de una empresa
tenemos que conseguir que los dos se queden con exactamente lo mismo
40 20 25 5 10
'''
def esFactible(solucion, valores, etapa, intento, exito, contadorAmbos):
    contador=0
    for i in valores:
        contador= contador+i

    #si es la etapa ultima, tienen que ser iguales por narices
    if etapa==4 and (contadorAmbos[intento]+valores[etapa]!=(contador//2)):
        print(contadorAmbos)
        return False

    #si estamos por la mitad, no se puede superar la mitad
    if etapa<4 and( contadorAmbos[intento]+valores[etapa])> (contador//2):
        return False

    return True


def BT(solucion, valores, etapa, contadorAmbos):
    intento=0
    exito=False
    while intento<2 and not exito: #intento es hombre1 o hombre2
        #es factible ponerlo como opcion
        if esFactible(solucion, valores, etapa, intento, exito,contadorAmbos):
            #marcamos
            solucion[etapa]=intento
            contadorAmbos[intento]= contadorAmbos[intento]+ valores[etapa]
            #si hemos llegado al final
            if etapa==4:
                print(solucion)
                exito= True
            else:
                #si no hemos llegado, pues seguimos avanzando
                exito= BT(solucion, valores, etapa+1, contadorAmbos)
            if exito==False:
                #desmarcamos
                solucion[etapa]='-'
                contadorAmbos[intento] = contadorAmbos[intento] - valores[etapa]
        intento= intento+1
    return exito
### main program ###
'''
la solucion va a ser un array lleno de 1 o 2
la etapa es cada una de las posiciones del array
el intento es 1 o 2
'''

solucion= ['-']*5
tam=5
valores=[40,20,25,5,10]
contadorAmbos=[0,0]

exito= BT(solucion, valores, 0, contadorAmbos)
print(solucion)