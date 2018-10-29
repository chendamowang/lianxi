# -*- coding: utf -8 -*-
from PrioQueue import PrioQueue

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'F': 6, 'E': 3},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

def init_distance(graph, s):
    distance = {s: 0}
    for key in graph:
        if key != s:
            distance[key] = float("inf")
    return distance


def dijkstra(graph, s):
    pq = PrioQueue()
    pq.enqueue((0, s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)

    while not pq.is_empty():
        pair = pq.dequeue()
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        nodes = graph[vertex].keys()
        for i in nodes:
            if i not in seen:
                if dist+graph[vertex][i] < distance[i]:
                    distance[i] = dist+graph[vertex][i]
                    parent[i] = vertex
                    pq.enqueue((dist+graph[vertex][i], i))
    return parent, distance

a, b = dijkstra(graph, 'A')
print a
print b