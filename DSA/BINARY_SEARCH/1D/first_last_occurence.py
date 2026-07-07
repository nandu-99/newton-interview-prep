# Last occurrence in a sorted array

# Problem Statement: Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1. Note: Consider 0 based indexing

# Example 1:
# Input: N = 7, target = 13, array[] = {3, 4, 13, 13, 13, 20, 40}  
# Output: 4  
# Explanation: The target value 13 appears for the first time at index number 2 in the array.  

arr = list(map(int, input().split()))
x = int(input())

def first_occurence(arr, x):
    l, h = 0, len(arr)-1 
    ans = -1
    while l<=h:
        m = (l+h)//2 
        if arr[m]==x:
            ans = m 
            h = m-1 
        elif arr[m]<x:
            l = m+1 
        else:
            h = m-1 
    return ans 

def last_occerence(arr, x):
    l, h = 0, len(arr)-1 
    ans = -1
    while l<=h:
        m = (l+h)//2 
        if arr[m]==x:
            ans = m 
            l = m+1 
        elif arr[m]<x:
            l = m+1
        else:
            h = m-1 
    return ans

print(first_occurence(arr, x), last_occerence(arr, x))
