# Dynamic Programming : Climbing Stairs

# Problem Statement: Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair. At a time we can climb either one or two steps. We need to return the total number of distinct ways to reach from 0th to Nth stair.

# Input: n = 2
# Output: 2
# Explanation: There are 2 unique ways to climb to the 2nd step:
# 1. 1 step + 1 step
# 2. 2 steps

n = int(input())

def climbing(n):
    d = {}
    def recur(i):
        if i==n:return 1 
        if i>n:return 0 
        if i in d:return d[i]
        d[i] = recur(i+1)+recur(i+2)
        return d[i]
    return recur(0)

print(climbing(n))
