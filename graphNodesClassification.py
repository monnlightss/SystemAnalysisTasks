from io import StringIO
import csv

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    graph = []
    for row in reader:
        graph.append(row)
    for x in graph:
        for y in x:
            y = int(y)

    #r1 - прямое управление
    arr1 = []
    for x in graph:
        if x[0] not in arr1:
            arr1.append(str(x[0]))

    #r2 - прямое подчинение
    arr2 = []
    for x in graph:
        if x[1] not in arr2:
            arr2.append(str(x[1]))

    #r3 - опосредованное управление
    f = graph
    g = graph
    arr3 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] not in arr3 and f[i][1] == g[j][0]:
                arr3.append(str(f[i][0]))

    #r4 - опосредованное подчинение
    arr4 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] not in arr4 and f[i][0] == g[j][1]:
                arr4.append(str(f[i][1]))

    #r5 - соподчинение
    arr5 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] not in arr5 and f[i][0] == g[j][0]:
                arr5.append(str(f[i][1]))

    return [arr1, arr2, arr3, arr4, arr5]
