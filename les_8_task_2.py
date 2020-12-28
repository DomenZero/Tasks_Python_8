'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
'''

from collections import deque
from collections import namedtuple

g=[
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0],
]

def dkstra(graph, start):
    length=len(graph)
    is_visited=[False]*length
    cost=[float('inf')]*length
    parent=[-1]*length

    cost[start]=0
    min_cost=0
    min_vertex=start
    next_vertex=[]
    way = deque([range(length)])

    path = [[]]
    result = [[] for _ in range(length)]

    while min_cost<float('inf'):
        is_visited[start]=True

        for i,vertex in enumerate(graph[start]):
            if vertex!=0 and not is_visited[i]:

                if cost[i]>vertex+cost[start]:
                    cost[i]=vertex+cost[start]
                    parent[i]=start
        min_cost=float('inf')
        for i in range(length):
            if min_cost>cost[i] and not is_visited[i]:

                if min_cost!='inf':
                    next_vertex.append([i])
                    # print(parent[i], i, cost[i])
                min_cost=cost[i]
                start=i

            if is_visited[i]:
                result[i].append(i)
                j = i
                while parent[j] != -1:
                    result[i].append(parent[j])
                    j = parent[j]


    for i in range(length):
        if is_visited[i]:
            print(list(set(result[i])))

    return cost


s=int(input('От какой вершины идти: '))
print(dkstra(g,s))
