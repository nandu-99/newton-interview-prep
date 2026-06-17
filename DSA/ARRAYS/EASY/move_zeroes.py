# Move all Zeros to the end of the array

# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

# Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
# Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
# Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

arr = list(map(int, input().split()))

def move_zeroes(arr):
    j= -1 
    for i in range(len(arr)):
        if arr[i]==0:
            j = i 
            break 
    
    for i in range(j+1, len(arr)):
        if arr[i]!=0:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1 
    return arr 

print(move_zeroes(arr))
