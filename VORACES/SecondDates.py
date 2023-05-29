'''
SECOND DATES
algoritmo voraces
'''
import copy


def voraz(listadoOrdenado, tamGrupo, numeroParticipantes):
    # solucion
    grupo1=[]
    grupo2=[]

    #cogemos el minimo de los dos grupos y es el que empezamos a meter gente primero
    tamOtroGrupo= numeroParticipantes-tamGrupo
    primerGrupo= min(tamOtroGrupo, tamGrupo)

    while len(grupo1)<primerGrupo:
        valor= listadoOrdenado[0]
        listadoOrdenado.remove(valor)
        grupo1.append(valor[0])

    for i in range(tamOtroGrupo):
        grupo2.append(listadoOrdenado[0][0])
        listadoOrdenado.remove(listadoOrdenado[0])

    print(*grupo1)
    print(*grupo2)

### main programa ###
primeraLinea= input().split(" ")
numeroParticipantes= int(primeraLinea[0])
tamGrupo= int(primeraLinea[1])

listado=[]

for i in range(numeroParticipantes):
    trozo=input().split(" ")
    tupla= (trozo[0], int(trozo[1]))
    listado.append(tupla)

listadoOrdenado= sorted(listado, key=lambda x: x[1])
voraz(listadoOrdenado, tamGrupo, numeroParticipantes)


'''
5 2
JamesLineberger 55
JeanetteMaurey 73
ChristieDangelo 29
HeatherTrew 78
LeolaSwift 30
'''