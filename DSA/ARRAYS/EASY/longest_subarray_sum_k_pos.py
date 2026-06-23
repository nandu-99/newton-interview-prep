# Longest Subarray with given Sum K(Positives)

# Problem Statement: Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

# Example 1:
# Input: nums = [10, 5, 2, 7, 1, 9], k = 15  
# Output: 4  
# Explanation: The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

arr = list(map(int, input().split()))
k = int(input())

# def longest_subarray(arr, k):
#     n = len(arr)
#     maxi = 0 
#     left =0 
#     right = 0 
#     summ = arr[0]
#     while right<n:
#         while left<=right and summ>k:
#             summ-=arr[left]
#             left+=1 
#         if summ==k:
#             maxi = max(maxi, right-left+1)
#         right+=1 
#         if right<n:
#             summ+=arr[right]
#     return maxi ]

def longest_subarray(arr, k):
    summ = 0 
    maxi =0 
    d = {} 
    for i in range(len(arr)):
        summ+=arr[i]
        if summ==k:
            maxi = i+1 
        rem = summ-k 
        if rem in d:
            leng = i-d[rem]
            maxi = max(maxi, leng)
        if summ not in d:
            d[summ] = i 
    return maxi 


print(longest_subarray(arr, k))
