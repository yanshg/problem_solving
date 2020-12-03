#!/usr/bin/python

"""

Find longest sequence formed by adjacent numbers in the matrix

For example, if we are at location (x, y) in the matrix, we can move to (x, y+1), (x, y-1), (x+1,y) or (x-1, y).

if the value at destination cell is one more than the value at source cell

The longest sequence formed by adjacent numbers in below matrix is 2 - 3 - 4 - 5 - 6 - 7

"""

def get_adjacent_seq(matrix,i,j,memo):
    rows,cols = len(matrix),len(matrix[0])
    if i<0 or i>=rows or j<0 or j>=cols:
        return []

    key = (i,j)
    if key in memo:
        return memo[key]

    path = []

    # Note: could not use abs(), otherwise run into infinite loop
    if j>0 and matrix[i][j-1]-matrix[i][j] == 1:
        path = get_adjacent_seq(matrix,i,j-1,memo)

    if j<cols-1 and matrix[i][j+1]-matrix[i][j] == 1:
        path = get_adjacent_seq(matrix,i,j+1,memo)

    if i>0 and matrix[i-1][j]-matrix[i][j] == 1:
        path = get_adjacent_seq(matrix,i-1,j,memo)

    if i<rows-1 and matrix[i+1][j]-matrix[i][j] == 1:
        path = get_adjacent_seq(matrix,i+1,j,memo)

    path = [ matrix[i][j] ] + path
    memo[key] = path
    return path

def get_longest_adjacent_seq(matrix):
    rows,cols = len(matrix),len(matrix[0])
    max_len = 0
    max_path = None
    memo = dict()
    for i in range(rows):
        for j in range(cols):
            path = get_adjacent_seq(matrix, i, j, memo)
            if path and len(path) > max_len:
                max_len = len(path)
                max_path = path
    return ' - '.join(map(str, max_path))


matrix = [ [ 10, 13, 14, 21, 23 ],
           [ 11, 9,  22, 2,  3  ],
           [ 12, 8,  1,  5,  4  ],
           [ 15, 24, 7,  6,  20 ],
           [ 16, 17, 18, 19, 25 ] ]

assert get_longest_adjacent_seq(matrix) == '2 - 3 - 4 - 5 - 6 - 7'
