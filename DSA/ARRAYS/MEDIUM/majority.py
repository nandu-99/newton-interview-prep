# Find the Majority Element that occurs more than N/2 times

# Problem Statement: Given an integer array nums of size n, return the majority element of the array.

# The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

# Example 1:
# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
# Output: 7  
# Explanation: The number 7 appears 5 times in the 9-sized array, making it the most frequent element.

arr = list(map(int, input().split()))

def majority(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i, 0)+1 
    for i in d:
        if d[i]>(len(arr)//2):
            return i 
    return -1 

print(majority(arr))

