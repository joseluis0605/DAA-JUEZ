'''
algoritmo voraz
'''
def voraz(candidatos, numeroParticipantes, grupoMenor):
    #solucion
    grupoChico=[]
    grupoGrande=[]

    #candidatos ordenados
    candidatos= sorted(candidatos, key= lambda x:x[1])


    tamGrupoChico= grupoMenor
    tamGrupoGrande= numeroParticipantes-grupoMenor

    for i in range(tamGrupoChico):
        grupoChico.append(candidatos[0][0])
        candidatos.remove(candidatos[0])
    for i in range(tamGrupoGrande):
        grupoGrande.append(candidatos[0][0])
        candidatos.remove(candidatos[0])

    print(*grupoChico)
    print(*grupoGrande)

if __name__=='__main__':
    primeraLinea= input().split(" ")
    numeroParticipantes= int(primeraLinea[0])
    grupoMenor= int(primeraLinea[1])

    candidatos=[]
    for i in range(numeroParticipantes):
        linea= input().split(" ")
        tupla= (linea[0], int(linea[1]))
        candidatos.append(tupla)
    voraz(candidatos, numeroParticipantes, grupoMenor)
'''
5 2
JamesLineberger 55
JeanetteMaurey 73
ChristieDangelo 29
HeatherTrew 78
LeolaSwift 30
'''