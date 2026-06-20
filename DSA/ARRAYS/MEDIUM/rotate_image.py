# Rotate Image by 90 degree

# Problem Statement: Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. The rotation must be done in place, meaning the input 2D matrix must be modified directly..

# Input :matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output : matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]


def rotate(matrix):
    m= len(matrix)
    for i in range(m):
        for j in range(i+1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(m):
        matrix[i] = matrix[i][::-1]
    return matrix



print(rotate(matrix))
