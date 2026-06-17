# Find the Largest element in an array

# Problem Statement: Given an array, we have to find the largest element in the array.

# Example 1:
# Input: arr[] = {2, 5, 1, 3, 0}  
# Output:5  
# Explanation: 5 is the largest element in the array.

arr = list(map(int, input().split()))

def largest(arr):
    maxi = float("-inf")
    for i in arr:
        if i>maxi:
            maxi = i 
    return maxi 

print(largest(arr))
