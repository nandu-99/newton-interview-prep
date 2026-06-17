# Count Maximum Consecutive One's in the array

# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..

# Example 1:
# Input: prices = {1, 1, 0, 1, 1, 1}
# Output: 3
# Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

arr = list(map(int, input().split()))

def maximum_ones(arr):
    maxi = 0 
    count = 0 
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1 
        else:
            count = 0 
    maxi = max(maxi, count)
    return maxi 

print(maximum_ones(arr))
