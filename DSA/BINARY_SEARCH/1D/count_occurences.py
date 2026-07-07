# Count Occurrences in Sorted Array

# Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

# Example 1:
# Input:
#  N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
# Output
# : 4
# Explanation:
#  3 is occurring 4 times in 
# the given array so it is our answer.

arr = list(map(int, input().split()))
x = int(input())

def occurence(arr, x, pos):
    l, h = 0, len(arr)-1 
    ans = -1
    while l<=h:
        m = (l+h)//2 
        if arr[m]==x:
            ans = m
            if pos=="first":
                h = m-1 
            else:
                l = m+1 
        elif arr[m]<x:
            l = m+1 
        else:
            h = m-1 
    return ans 

first = occurence(arr, x, "first")
if first==-1:
    print(-1, -1) 
else:
    last = occurence(arr, x, "last")
    print(last-first+1)
