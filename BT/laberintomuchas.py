'''
BT del laberinto con muchas posibilidades
'''
def imprimir(tablero):
    for i in tablero:
        print(*i)

def esFactible(tablero,etapa, miMovimiento, intento):
    if etapa[0]<0 or etapa[0]>4 or etapa[1]<0 or etapa[1]>4:
        return False
    if tablero[etapa[0]][etapa[1]]=='S' or tablero[etapa[0]][etapa[1]]=='-':
        return True
    else:
        return False

def BT(tablero,etapa, movimientos):
    intento=0
    while intento<4:
        #es factible realizar este movimiento para ello hay que calcular la posicion nueva
        miMovimiento= movimientos[intento]
        filaNueva= etapa[0]+miMovimiento[0]
        columnaNueva= etapa[1]+miMovimiento[1]
        if esFactible(tablero, (filaNueva,columnaNueva), miMovimiento, intento):
            #vamos a marcar, pero antes tenemos que guardar el anterior
            old= tablero[filaNueva][columnaNueva]
            tablero[filaNueva][columnaNueva]='X'
            #hemos llegado?
            if old=='S':
                tablero[filaNueva][columnaNueva]='S'
                imprimir(tablero)
                input()
            else:
                BT(tablero, (filaNueva,columnaNueva), movimientos)
            #vamos a desmarcar
            if old!= 'S':
                tablero[filaNueva][columnaNueva]='-'
        intento= intento+1


if __name__=='__main__':
    tablero=[]
    for i in range(5):
        fila=['-']*5
        tablero.append(fila)

    movimientos=[(1,0),(0,1),(-1,0), (0,-1)]

    tablero[1][1] = 'M'
    tablero[1][2] = 'M'
    tablero[1][3] = 'M'
    tablero[2][1] = 'M'
    tablero[2][2] = 'M'
    tablero[0][0] = 'X'
    tablero[4][2] = 'S'

    BT(tablero,(0,0), movimientos)
    imprimir(tablero)