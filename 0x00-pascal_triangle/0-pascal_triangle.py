#!/usr/bin/python3
"""
Creates a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
"""

def pascal_triangle(n):
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res

