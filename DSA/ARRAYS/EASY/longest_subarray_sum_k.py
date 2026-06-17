# Length of the longest subarray with zero Sum
# Problem Statement: Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.

# Example 1:
# Input: N = 6, array[] = {9, -3, 3, -1, 6, -5}  
# Result: 5  
# Explanation:
#  The following subarrays sum to zero:
# - {-3, 3}
# - {-1, 6, -5}
# - {-3, 3, -1, 6, -5}
# The length of the longest subarray with sum zero is 5.

arr = list(map(int, input().split()))
k = int(input())

def longest_subarray(arr, k):
    first_occurrence = {}
    maxi = 0 
    prefix_sum = 0 
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum==k:
            maxi = i+1 
        rem = prefix_sum-k 
        if rem in first_occurrence:
            maxi = max(maxi, i-first_occurrence[rem])
        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum] = i 
    return maxi 

print(longest_subarray(arr, k))
        
