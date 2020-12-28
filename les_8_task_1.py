'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было? Примечание. Решите задачу при помощи построения графа.
4-6,3-3
'''


def build(number):
    start = 0
    graph = []
    i = 1
    handshake = 0
    if number <= 2:
        return number - 1, [number - 1]

    while start <= number - 1:
        while i <= number - 1:
            if (i != start):
                graph.append([start, i])
                handshake += 1
            i += 1
        start += 1
        i = start + 1
    return handshake, graph


num = int(input('Количество друзей: '))
hand, graph = build(num)
print(f'Рукопожатий: {hand}')
print(*graph, sep='\n')
