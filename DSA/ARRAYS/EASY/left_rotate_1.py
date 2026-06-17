# Left Rotate the Array by One

# Problem Statement: Given an integer array nums, rotate the array to the left by one.

# Note: There is no need to return anything, just modify the given array.

# Example 1:
# Input: nums = [1, 2, 3, 4, 5]  
# Output: [2, 3, 4, 5, 1]  
# Explanation: Initially, nums = [1, 2, 3, 4, 5]  
# Rotating once to the left results in nums = [2, 3, 4, 5, 1].

arr = list(map(int, input().split()))

def left_rotate(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[-1]=temp
    return arr 

print(left_rotate(arr))
