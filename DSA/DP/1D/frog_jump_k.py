# Dynamic Programming: Frog Jump with k Distances (DP 4)

# Problem Statement:

# A frog wants to climb a staircase with n steps. Given an integer array heights, where heights[i] contains the height of the ith step, and an integer k. To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy, where abs() denotes the absolute difference. The frog can jump from the ith step to any step in the range [i + 1, i + k], provided it exists. Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.

# Example 1:
# Input: heights = [10, 5, 20, 0, 15], k = 2
# Output: 15
# Explanation:
# 0th step -> 2nd step, cost = abs(10 - 20) = 10
# 2nd step -> 4th step, cost = abs(20 - 15) = 5
# Total cost = 10 + 5 = 15.

def frog_jump_k(arr, k):
    d = {}
    def recur(i):
        if i in d:return d[i]
        if i<=0:return 0 
        mini = float('inf')
        for j in range(1, k+1):
            if i-j>=0:
                jump = recur(i-j)+abs(arr[i]-arr[i-j])
                mini = min(mini, jump)
        d[i]= mini 
        return d[i]
    return recur(len(arr)-1)

print(frog_jump_k([10, 5, 20, 0, 15], 2))
