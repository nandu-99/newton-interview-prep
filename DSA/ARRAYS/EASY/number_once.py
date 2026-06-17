# Find the number that appears once, and the other numbers twice

# Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

# Example 1:
# Input Format: arr[] = {4,1,2,1,2}
# Result: 4
# Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.

arr = list(map(int, input().split()))


def number_once(arr):
    # using xor
    x = 0 
    for i in arr:
        x^=i 
    return x


    d = {}
    for i in arr:
        d[i] = d.get(i, 0)+1 
    for i in d:
        if d[i]==1:
            return i 
    return -1 



print(number_once(arr))
