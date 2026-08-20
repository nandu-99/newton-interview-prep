# Grid Unique Paths : DP on Grids (DP8)

# Problem Statement: Given two integers m and n, representing the number of rows and columns of a 2d array named matrix. Return the number of unique ways to go from the top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).

# Movement is allowed only in two directions from a cell: right and bottom.

# Example 1:
# Input:
#  m = 3, n = 2  
# Output:
#  3  
# Explanation:
#  There are 3 unique ways to go from the top-left to the bottom-right cell:
# 1) right → down → down  
# 2) down → right → down  
# 3) down → down → right  

m, n = map(int, input().split())

def unique(m, n):
    d = {}
    def recur(i, j):
        if i==m-1 and j==n-1:return 1 
        if i>=m or j>=n:return 0 
        if (i, j) in d:return d[(i, j)]
        d[(i, j)] = recur(i+1, j) + recur(i, j+1)
        return d[(i, j)]
    return recur(0, 0)

print(unique(m, n))
