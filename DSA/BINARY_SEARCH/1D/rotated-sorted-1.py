# Search Element in a Rotated Sorted Array

# Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

# Input:nums = [4, 5, 6, 7, 0, 1, 2], k = 0
# Output :4
# Explanation : Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

arr = list(map(int, input().split()))
x = int(input())

def rotated_sorted(arr, x):
    l, h = 0, len(arr)-1 
    while l<=h:
        m = (l+h)//2 
        if arr[m]==x:
            return m 
        if arr[l]<arr[m]:
            if arr[l]<=x<arr[m]:
                h = m-1 
            else:
                l = m+1 
        else:
            if arr[m]<x<=arr[h]:
                l = m+1 
            else:
                h = m-1 
    return -1

print(rotated_sorted(arr, x))
