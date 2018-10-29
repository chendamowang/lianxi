# -*- coding:utf-8 -*-
"""
迷宫求解
"""

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

def possible(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print pos,
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if possible(maze, nextp):
            if find_path(maze, nextp, end):
                print pos,
                return True
    return False

maze = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]]

find_path(maze, (1,1), (3,3))