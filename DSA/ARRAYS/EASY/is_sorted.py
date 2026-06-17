# Check if an Array is Sorted

# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: True.
# Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

arr = list(map(int, input().split()))

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i]<arr[i-1]:
            return False 
    return True 

print(is_sorted(arr))
