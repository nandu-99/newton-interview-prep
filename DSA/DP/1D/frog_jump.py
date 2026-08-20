# Dynamic Programming : Frog Jump (DP 3)

# Problem Statement: Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1..

# Example 1:
# Input: heights = [2, 1, 3, 5, 4]
# Output: 2
# Explanation: One possible route can be,
# 0th step -> 2nd Step = abs(2 - 3) = 1
# 2nd step -> 4th step = abs(3 - 4) = 1
# Total = 1 + 1 = 2.

def frog_jump(arr):
    d = {}
    def recur(i):
        if i<=0:return 0 
        if i in d:return d[i]
        one = two = float('inf')
        if i-1>=0:
            one = recur(i-1)+abs(arr[i]-arr[i-1])
        if i-2>=0:
            two = recur(i-2)+abs(arr[i]-arr[i-2])
        d[i] = min(one, two)
        return d[i]
    return recur(len(arr)-1)

print(frog_jump([2, 1, 3, 5, 4]))
