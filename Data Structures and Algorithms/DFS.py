# -*- coding: utf -8 -*-
from stack import SStack
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'F', 'E'],
    'E': ['C', 'D'],
    'F': ['D']
}

def dfs(graph, s):
    stack = SStack()
    stack.push(s)
    seen = set()
    seen.add(s)
    parent = {s: None}
    while not stack.is_empty():
        vertex = stack.pop()
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                stack.push(i)
                seen.add(i)
                parent[i] = vertex
        print vertex
    return parent

parent = dfs(graph, 'A')
v = 'F'
print '\n'
while v:
    print v
    v = parent[v]