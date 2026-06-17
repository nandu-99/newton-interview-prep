# Linear Search in C

# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

# Example 1:
# Input: arr[] = 1 2 3 4 5, num = 3  
# Output: 2  `
# Explanation: 3 is present at the 2nd index of the array.

arr = list(map(int, input().split()))
tar = int(input())

def search(arr, tar):
    for i in range(len(arr)):
        if arr[i]==tar:
            return i 
    return -1 

print(search(arr, tar))
