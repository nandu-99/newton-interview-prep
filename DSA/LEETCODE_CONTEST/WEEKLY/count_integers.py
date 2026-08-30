# 4038. Count Integers Appearing in a Single Block

# Easy

# You are given an integer array nums.

# An integer x is special if all occurrences of x in nums appear in a single contiguous block.

# Return the number of distinct special integers in nums.

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
