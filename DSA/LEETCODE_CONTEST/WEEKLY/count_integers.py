# 4038. Count Integers Appearing in a Single Block

# Easy

# You are given an integer array nums.

# An integer x is special if all occurrences of x in nums appear in a single contiguous block.

# Return the number of distinct special integers in nums.

# Example 1:

# Input: nums = [1,2,2,1]

# Output: 1

# Explanation:

# 1 appears at indices 0 and 3, forming two separate blocks, so it is not special.
# 2 appears in a single contiguous block at indices [1, 2], so it is special.
# Therefore, there is one special integer.

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                d[nums[i]] = d.get(nums[i], 0)+1
        count = 0 
        for i in d:
            if d[i]==1:
                count+=1 
        return count
