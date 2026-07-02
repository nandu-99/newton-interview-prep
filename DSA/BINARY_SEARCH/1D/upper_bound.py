# Implement Upper Bound

# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.

# What is Upper Bound?
# The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.

# The upper bound is the smallest index, ind, where arr[ind] > x.

# Example 1:
# Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
# Result: 3
# Explanation: Index 3 is the smallest index such that arr[3] > x.

# Example 2:
# Input Format: N = 6, arr[] = {3,5,8,9,15,19}, x = 9
# Result: 4
# Explanation: Index 4 is the smallest index such that arr[4] > x.

arr = list(map(int, input().split()))
x = int(input())

def upper_bound(arr, x):
    l, h = 0, len(arr)-1 
    ans = -1
    while l<=h:
        m = (l+h)//2 
        if arr[m]>x:
            ans = m 
            h = m-1 
        else:
            l = m+1 
    return ans 

print(upper_bound(arr, x))
