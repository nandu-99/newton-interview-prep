# Union of Two Sorted Arrays

# Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

# The union of two arrays can be defined as the common and distinct elements in the two arrays.

# NOTE: Elements in the union should be in ascending order.

# Input:n = 5,m = 5 arr1[] = {1,2,3,4,5}  arr2[] = {2,3,4,4,5}
# Output: {1,2,3,4,5}
# Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
# Distnict Elements in arr1 are : 1
# Distnict Elemennts in arr2 are : No distinct elements.
# Union of arr1 and arr2 is {1,2,3,4,5}

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def union(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set1 | set2 

print(union(arr1, arr2))
