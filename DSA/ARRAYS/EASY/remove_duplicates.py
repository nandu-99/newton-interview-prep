# Remove Duplicates in-place from Sorted Array

# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

# Input: arr[]=[1,1,2,2,2,3,3]
# Output: [1,2,3,_,_,_,_]
# Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

arr = list(map(int, input().split()))

def remove_duplicates(arr):
    i = 0 
    for j in range(1, len(arr)):
        if arr[j]!=arr[i]:
            i+=1 
            arr[i] = arr[j]
    return i+1 

k = remove_duplicates(arr)
print(arr[:k])
