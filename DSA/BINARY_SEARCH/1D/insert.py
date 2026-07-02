# Search Insert Position

# Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

# Example 1:
# Input Format: arr[] = {1,2,4,7}, x = 6
# Result: 3
# Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

arr = list(map(int, input().split()))
x = int(input())

def insert(arr, x):
    l, h = 0, len(arr)-1 
    ans= len(arr)
    while l<=h:
        m = (l+h)//2 
        if arr[m]>=x:
            ans = m 
            h = m-1 
        else:
            l = m+1 
    return ans 

print(insert(arr, x))
