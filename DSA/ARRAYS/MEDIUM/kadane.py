# Kadane's Algorithm : Maximum Subarray Sum in an Array

# Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [2, 3, 5, -2, 7, -4]  
# Output: 15  
# Explanation: The subarray from index 0 to index 4 has the largest sum = 15, which is the maximum sum of any contiguous subarray.

arr = list(map(int, input().split()))

def kadane(arr):
    maxi = float('-inf')
    curr = 0 
    for i in arr:
        curr+=i 
        maxi = max(maxi, curr)
    return maxi 

print(kadane(arr))
