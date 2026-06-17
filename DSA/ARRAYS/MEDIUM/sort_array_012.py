# Sort an array of 0s, 1s and 2s

# Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.

# Input: nums = [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]
# Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

arr = list(map(int, input().split()))

def sort_array(arr):
    c0 = 0 
    c1 = 0 
    c2 = 0 
    for i in arr:
        if i==0:
            c0+=1 
        elif i==1:
            c1+=1 
        elif i==2:
            c2+=1 
    for i in range(c0):
        arr[i] = 0 
    for i in range(c0, c0+c1):
        arr[i] = 1
    for i in range(c0+c1, len(arr)):
        arr[i] = 2 
    return arr 

print(sort_array(arr))
