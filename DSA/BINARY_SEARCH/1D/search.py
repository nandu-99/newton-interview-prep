# Binary Search: Explained

# Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the given array. Assume the given array does not contain any duplicate numbers.

arr = list(map(int, input().split()))
x = int(input())

def binary_search(arr, x):
    l, h = 0, len(arr)-1 
    while l<=h:
        m = (l+h)//2 
        if arr[m]==x:
            return m
        elif arr[m]>x:
            h = m-1
        else:
            l = m+1
    return -1 

print(binary_search(arr, x))
