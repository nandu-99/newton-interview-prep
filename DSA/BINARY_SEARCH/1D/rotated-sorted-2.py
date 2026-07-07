# Search Element in Rotated Sorted Array II

# Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

# Example 1:
# Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
# Result: True
# Explanation: The element 3 is present in the array. So, the answer is True.

arr = list(map(int, input().split()))
x = int(input())

def rotated_sorted(arr, x):
    l, h = 0, len(arr)-1 
    while l<=h:
        m = (l+h)//2 
        if arr[m]==x:
            return True 
        if arr[l]==arr[m]==arr[h]:
            l+=1
            h-=1 
            continue 
        if arr[l]<=arr[m]:
            if arr[l]<=x<=arr[m]:
                h=m-1 
            else:
                l = m+1 
        else:
            if arr[m]<=x<=arr[h]:
                l=m+1 
            else:
                h = m-1 
    return False

print(rotated_sorted(arr, x))
