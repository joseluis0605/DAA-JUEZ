def horario(lista):
    tam = len(lista)
    tareas = 0
    tiempo = -1
    for i in range(tam):
        if lista[i][1] > tiempo:
            tiempo = lista[i][2]
            tareas += 1
        i += 1
    print(tareas)

### main program
numeroTareas = int(input())
valores=[]

for _ in range(numeroTareas):
    nombre, inicio, fin = input().split()
    valores.append((str(nombre), int(inicio), int(fin)))
valores.sort(key=lambda x: x[2])
horario(valores)

