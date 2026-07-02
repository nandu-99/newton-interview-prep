# Implement Lower Bound

# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

# What is lower bound?
# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

# Example 1:
# Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
# Result: 1
# Explanation: Index 1 is the smallest index such that arr[1] >= x.

# Example 2:
# Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
# Result: 3
# Explanation: Index 3 is the smallest index such that arr[3] >= x.

arr = list(map(int, input().split()))
x = int(input())

def lower_bound(arr, x):
    l, h = 0, len(arr)-1 
    ans = -1
    while l<=h:
        m = (l+h)//2 
        if arr[m]>=x:
            ans = m 
            h = m-1 
        else:
            l = m+1 
    return ans 

print(lower_bound(arr, x))
