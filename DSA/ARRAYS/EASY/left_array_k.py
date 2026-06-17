# Rotate array by K elements

# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

# Input : nums = [1, 2, 3, 4, 5, 6, 7], k = 2, right
# Output : [6, 7, 1, 2, 3, 4, 5]
# Explanation : rotate 1 step to the right: [7, 1, 2, 3, 4, 5, 6]
# rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5] 

# Input : nums = [1, 2, 3, 4, 5, 6], k=2, left
# Output : [3, 4, 5, 6, 1, 2]
# Explanation :rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

arr = list(map(int, input().split()))
k = int(input())
dir = input()

def reverse(arr, start, end):
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1 
        end-=1 


def rotate(arr, k, dir):
    k = k%len(arr)
    if dir=="right":
        reverse(arr, 0, len(arr)-1)
        reverse(arr, 0, k-1)
        reverse(arr, k, len(arr)-1)
    else:
        reverse(arr, 0, k-1)
        reverse(arr, k, len(arr)-1)
        reverse(arr, 0, len(arr)-1)
    return arr 

print(rotate(arr, k, dir))
