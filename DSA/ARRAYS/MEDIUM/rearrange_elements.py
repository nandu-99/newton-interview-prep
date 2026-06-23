# Rearrange Array Elements by Sign

# Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# Example 1:
# Input:
# arr[] = {1,2,-4,-5}, N = 4
# Output:
# 1 -4 2 -5
# Explanation: 
# Positive elements = 1,2
# Negative elements = -4,-5
# To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

arr = list(map(int, input().split()))
n = int(input())

def rearrange(arr, n):
    ans = [0]*n
    posi = 0 
    negi = 1 
    for i in range(len(arr)):
        if arr[i]<0:
            ans[negi] = arr[i]
            negi+=2
        else:
            ans[posi] = arr[i]
            posi+=2 
    return ans 

print(rearrange(arr, n))
            

