'''
ALGORITMO DE BT

intento: colocar la reina en cada una de las filas
etapa:va a ser cada una de las reinas que hay que colocar, cada fila del tablero
solucion: va a ser una matriz, un tablero
'''

def esFactible(solucion, exito, intento, etapa):

    #protegemos las verticales
    for i in range(etapa):
        #nos recorremos hasta la etapa
        if solucion[i][intento]=='X':
            return False

    # protegemos las diagonales hacia la derecha
    fila = etapa - 1
    columna = intento - 1
    while fila >= 0 and columna >= 0:
        if solucion[fila][columna] == 'X':
            return False
        fila = fila - 1
        columna = columna - 1

    # protegemos la derecha de la diagonal
    fila = etapa - 1
    columna = intento + 1
    while fila >= 0 and columna < 8:
        if solucion[fila][columna] == 'X':
            return False
        fila = fila - 1
        columna = columna + 1


    return True


def BT(solucion, etapa):
    exito=False
    intento=0
    while intento<=7 and not exito:
        #es factible poner la reina ahi
        if esFactible(solucion, exito, intento, etapa):
            #si es factible marcamos
            solucion[etapa][intento]='X'
            #es la ultima fila del tablero?
            if etapa==7:

                exito= True
                #termina ya que se ha completado nuestro tablero
            else:
                #no se ha completado, pues seguimos tirando para abajo
                exito= BT(solucion, etapa+1)
            if exito==False:
                #si hemos recibido un falso de exito, deshacemos y probamos por otra rama
                solucion[etapa][intento]='-'
        intento= intento+1
    return exito


def imprimir(tablero):
    for i in tablero:
        print(*i)

solucion=[]
for i in range(8):
    fila=['-']*8
    solucion.append(fila)

exito= BT(solucion, 0)
imprimir(solucion)

