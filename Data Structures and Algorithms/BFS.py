# -*- coding: utf -8 -*-
from queue import SQueue

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'F', 'E'],
    'E': ['C', 'D'],
    'F': ['D']
}

def bfs(graph, s):
    queue = SQueue()
    queue.enqueue(s)
    seen = set()
    seen.add(s)
    while not queue.is_empty():
        vertex = queue.dequeue()
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                queue.enqueue(i)
                seen.add(i)
        print vertex

bfs(graph, 'E')