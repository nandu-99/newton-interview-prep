# Find the Missing Number
# Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

# Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
# Output: 6
# Explanation: All the numbers from 1 to 8 are present except 6.

arr = list(map(int, input().split()))

def missing_number(arr):
    n = len(arr)+1
    expec = (n*(n+1))//2 
    actual = sum(arr)
    return expec-actual 

print(missing_number(arr))
