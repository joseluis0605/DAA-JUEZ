'''
algoritmo de BT en donde vamos a usar la peor opcion, es decir, la mas larga para llegar y asi recorrer todo
para ello vamos a llevar un contador
la solucion va a ser una matriz donde vamos a marcar
el intento va a ser el movimiento, arriba, abajo, derecha e izquierda
la etapa va a ser nuestra posicion
'''
def contar(tam, solucion):
    contador= 0
    for i in range(tam):
        for j in range(tam):
            if solucion[i][j]=='0':
                contador= contador+1
    return contador

def esFactible(solucion, tam, etapa, contadorPosicionesOcupar, cuenta, movimientos,intento, filaNueva, columnaNueva):
    #si nos salimos de los marcos del tablero
    if etapa[0]<0 or etapa[0]==tam or etapa[1]<0 or etapa[1]==tam:
        return False
    #si coincide la posicion con un 0 aceptamos
    if solucion[etapa[0]][etapa[1]]=='0':
        return True
    return False

def  BT(solucion, tam, etapa, contadorPosicionesOcupar, cuenta, movimientos):
    exito=False
    intento=0
    #mientras no tengamos exito y no superemos los intentos por posicion
    while not exito and intento<4:
        #calculamos la posicion actual
        miMovimiento= movimientos[intento]
        filaNueva= miMovimiento[0]+etapa[0]
        columnaNueva= miMovimiento[1]+etapa[1]
        if esFactible(solucion, tam, (filaNueva, columnaNueva), contadorPosicionesOcupar, cuenta, movimientos,intento, filaNueva, columnaNueva):
            #es factible realizar el movimiento, por lo que marcamos
            cuenta[0]= cuenta[0]+1
            solucion[filaNueva][columnaNueva]='X'
            #si hemos terminoado
            if cuenta[0]==contadorPosicionesOcupar and filaNueva==tam-1 and columnaNueva==tam-1:
                return True
            else:
                exito= BT(solucion, tam, (filaNueva, columnaNueva), contadorPosicionesOcupar, cuenta, movimientos)
            if not exito:
                #procedemos a desmarcar
                cuenta[0] = cuenta[0] - 1
                solucion[filaNueva][columnaNueva] = '0'
        intento= intento+1
    return exito


### main program ##
tam=int (input())
solucion=[]
for i in range(tam):
    linea= input().split(" ")
    solucion.append(linea)

#necesitamos los movimientos
movimientos=[(1,0),(-1,0),(0,1),(0,-1)]
contadorPosicionesOcupar= contar(tam, solucion)
cuenta=[1]
solucion[0][0]='X'



exito= BT(solucion, tam, (0,0), contadorPosicionesOcupar, cuenta, movimientos)
if exito:
    print('SI')
else:
    print("NO")