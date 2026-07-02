# Floor and Ceil in Sorted Array

# Problem Statement: ou're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1]. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x

# Example 1:
# Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
# Result: 4 7
# Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

arr = list(map(int, input().split()))
x = int(input())

def floor(arr, x):
    l, h = 0, len(arr)-1 
    ans = -1
    while l<=h:
        m = l+(h-l)//2 
        if arr[m]<=x:
            ans = arr[m]
            l = m+1 
        else:
            h = m-1 
    return ans 

def ceil(arr, x):
    l, h = 0, len(arr)-1 
    ans = -1
    while l<=h:
        m = l+(h-l)//2 
        if arr[m]>=x:
            ans = arr[m]
            h = m-1 
        else:
            l = m+1 
    return ans 


print(floor(arr, x), ceil(arr, x))

