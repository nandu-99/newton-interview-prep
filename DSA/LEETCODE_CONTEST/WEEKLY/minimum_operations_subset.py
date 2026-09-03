# 4040. Minimum Operations to Form Subset Sum I
# Medium

# You are given an integer array nums and an integer sum.

# In one operation, choose an element with current value x and replace it with either 2 * x or floor(x / 2).

# For each element, all multiplication operations performed on it must occur before any division operations performed on it.

# Return the minimum number of operations needed so that some subset of the resulting array has a sum exactly equal to sum. If it is impossible, return -1.

# The floor() function returns the integer part of the division.

# Example 1:

# Input: nums = [5,6,10], sum = 4

# Output: 3

# Explanation:

# Divide nums[0] = 5 twice: 5 → 2 → 1, costing 2 operations.
# Divide nums[1] = 6 once: 6 → 3, costing 1 operation.
# After these operations, nums = [1, 3, 10]. The subset {1, 3} sums to 4 using 3 operations in total.

class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        # d = {}
        
        # def recur(i, tar):
        #     if (i, tar) in d:return d[(i, tar)]
        #     if tar==0:return 0
        #     if i==len(nums) or tar<0:return float('inf')
        #     x = nums[i]
            
        #     ans = []
        #     div = x 
        #     c = 0 
        #     while div>0:
        #         if div<=tar:
        #             ans.append((div, c))
        #         div//=2 
        #         c+=1 

        #     mul = x*2 
        #     c = 1 
        #     while mul<=tar:
        #         ans.append((mul, c))
        #         mul*=2 
        #         c+=1 

        #     skip = recur(i+1, tar)

        #     for op, c in ans:
        #         skip = min(skip, c+recur(i+1, tar-op))
        #     d[(i, tar)] = skip 
        #     return skip 
        # final = recur(0, sum)
        # if final==float('inf'):
        #     return -1 
        # return final
        tar = sum 
        d = [float('inf')]*(tar+1)
        d[0] = 0 
        for x in nums:
            ans = []
            div = x 
            c = 0 
            while div>0:
                if div<=tar:
                    ans.append((div, c))
                div//=2 
                c+=1 

            mul = x*2 
            c = 1 
            while mul<=tar:
                ans.append((mul, c))
                mul*=2 
                c+=1 
            new = d[:]
            for op, c in ans:
                for s in range(tar, op-1, -1):
                    if d[s-op]+c<new[s]:
                        new[s] = d[s-op]+c 
            d = new 
        final = d[tar]
        if final==float('inf'): return -1 
        return final
