#!/usr/bin/python3
"""
Creates a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row
    
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        prev_row = triangle[i-1]
        
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])  # Calculate element based on previous row
            
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    
    return triangle
