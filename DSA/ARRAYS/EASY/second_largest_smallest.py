# Find Second Smallest and Second Largest Element in an array

# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

# Example 1:
# Input: [1, 2, 4, 7, 7, 5]  
# Output: Second Smallest : 2  , Second Largest : 5  
# Explanation: The elements are sorted as 1, 2, 4, 5, 7, 7.  
# Hence, the second smallest element is 2, and the second largest element is 5.

arr = list(map(int, input().split()))

def sec_smallest(arr):
    mini = float('inf')
    sec_mini = mini 
    for i in arr:
        if i<mini:
            sec_mini = mini 
            mini = i 
        elif i<sec_mini and i!=mini:
            sec_mini = i  
    return sec_mini 

def sec_largest(arr):
    maxi = float('-inf')
    sec_maxi = maxi 
    for i in arr:
        if i>maxi:
            sec_maxi = maxi 
            maxi = i 
        elif i>sec_maxi and i!=maxi:
            sec_maxi = i 
    return sec_maxi

print(sec_smallest(arr))
print(sec_largest(arr))
