'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''
import random

def gen_graph(n):
    return {x: list(random.randrange(1,n) if i != x else 0 for i in range(n)) for x in range(n)}

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

# n=7
n=int(input('введите число вершин: '))

x=0
gr2=gen_graph(n)
print(gr2)
visited = dfs(gr2,0,[])
print(visited)
