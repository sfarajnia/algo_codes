import csv
import numpy as np

def contraction(E, vertices):
    v = vertices
    e = E.copy()
    while v > 2:
        to_r = np.random.choice(len(e), 1)[0]
        edge = e[to_r] 
        i = 0
        while i < len(e):
            new_v =  set([min(edge)])
            if e[i].intersection(edge) != set():
                e[i] = (e[i].difference(edge)).union(new_v)
                if len(e[i]) == 1: 
                    e.remove(e[i])
                    i -= 1
            i += 1
        v -= 1
    return len(e)




with open('kargerMinCut.txt') as graph:
    g = csv.reader(graph, delimiter="\t")
    Edges = []
    E_dict = {}
    v = 0
    for line in g:
        v += 1
        line.remove("")
        l = list(map(int, line))
        e = [set([l[0], l[j]])
             for j in range(1, len(l)) if set([l[0], l[j]]) not in Edges]
        E_dict.update({l[0]: set(l[1:])})
        Edges.extend(e)
        
l = []
for i in range(2000):
    cut_num = contraction(Edges, v)
    l.append(cut_num)
    print(cut_num, i)

print(min(l))