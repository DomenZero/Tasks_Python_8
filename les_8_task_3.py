'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''
import random
from collections import defaultdict

def gen_graph(n):
    return {x: list(range(random.randint(1, n))) for x in range(n)}

def dfs(graph, start, visited):
    if start not in visited:
        visited.append(start)
        for n in graph[start]:
            dfs(graph,n, visited)
    return visited

# gr2={
#     0: {2,3},
#     1: {0,2,3},
#     2: {0,1},
#     3: {0},
#     4: {2,6},
#     5: {2,7},
#     6: {4},
#     7: {1, 2},
# }

n=int(input('введите число вершин: '))
i=0
gr=[]
while i<n:
    g = {random.randint(0,n) for i in range(random.randint(1,n))}

    gr.append({i:g})
    i+=1

x=0
gr2=gen_graph(n)
print(gr2)
visited = dfs(gr2,0,[])
print(visited)
