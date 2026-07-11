# Search in a sorted 2D matrix

# Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

# Input :mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
# Output :True.
# Explanation :The target = 8 exists in the 'mat' at index (1, 3).

matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
x = int(input())

def search(matrix, x):
    n = len(matrix)
    m = len(matrix[0])

    l = 0 
    h = n*m-1 

    while l<=h:
        mid = (l+h)//2 
        row = mid//m 
        col = mid%m 
        if matrix[row][col]==x:
            return True 
        if matrix[row][col]<x:
            l = mid+1 
        else:
            h = mid-1 
    return False 

print(search(matrix, x))
