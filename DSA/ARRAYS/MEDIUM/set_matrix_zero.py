# Set Matrix Zero

# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix..

# Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def set_matrix_zero(matrix):
    m, n = len(matrix), len(matrix[0])
    
    first_row_zero = False
    first_col_zero = False 

    for j in range(n):
        if matrix[0][j]==0:
            first_row_zero = True 
            break 
    for i in range(m):
        if matrix[i][0]==0:
            first_col_zero = True 
            break 
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j]==0:
                matrix[i][0] = 0 
                matrix[0][j] = 0 
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j] = 0 
    
    if first_row_zero:
        for i in range(n):
            matrix[0][i] = 0 
    
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0 

    return matrix

print(set_matrix_zero(matrix))
