# 4035. Maximum Valid Split Positions I

# Medium

# You are given an integer array nums.

# You may remove at most one element from nums. Let arr be the array of remaining elements in their original order, and let m be its length.

# A split position i of arr is valid if:

# 0 <= i < m - 1, and
# gcd(arr[0..i]) == gcd(arr[i + 1..m - 1]).
# An array of length 1 has no valid split positions.

# The score of arr is the number of valid split positions in it.

# Return the maximum possible score of arr.

# Here, gcd(a) denotes the greatest common divisor of all elements in the array a.

from math import gcd

class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        a = len(nums)

        def find_gcd(arr):
            b = len(arr)
            prearr = [0]*b 
            sufarr = [0]*b 
            for i in range(b):
                if i==0:
                    prearr[i]=arr[i]
                else:
                    prearr[i] = gcd(prearr[i-1], arr[i])
            for i in range(b-1, -1, -1):
                if i==b-1:
                    sufarr[i] = arr[i]
                else:
                    sufarr[i] = gcd(sufarr[i+1], arr[i])

            ans = 0 
            for i in range(b-1):
                if prearr[i]==sufarr[i+1]:
                    ans+=1 
            return ans 

        ans = find_gcd(nums)
        for i in range(a):
            arr = nums[:i]+nums[i+1:]
            ans = max(ans, find_gcd(arr))
        return ans
                    
                