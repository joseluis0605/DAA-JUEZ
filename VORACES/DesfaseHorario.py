def horario(data):
    data.sort(key=lambda a: a[2])
    n = len(data)
    tareas = 0
    act_time = -1
    for i in range(n):
        if data[i][1] > act_time:
            act_time = data[i][2]
            tareas += 1
        i += 1
    return tareas


n_tareas = int(input())

data = []

for _ in range(n_tareas):
    nombre, init, fin = input().split()
    data.append((str(nombre), int(init), int(fin)))

print(horario(data))

