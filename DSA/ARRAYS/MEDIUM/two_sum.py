# Two Sum : Check if a pair with given sum exists in Array

# Problem Statement: Given an array of integers arr[] and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

# Input: N = 5, arr[] = {2,6,5,8,11}, target = 14
# Output : YES
# Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for first variant for second variant output will be : [1,3].

arr = list(map(int, input().split()))
target = int(input())

def two_sum(arr, target):
    d = {}
    for i in range(len(arr)):
        comp = target-arr[i] 
        if comp in d:
            return (d[comp], i)
        d[arr[i]] = i 
    return -1 

print(two_sum(arr, target))
    
