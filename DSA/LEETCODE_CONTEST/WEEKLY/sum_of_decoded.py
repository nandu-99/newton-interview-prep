# 4039. Sum of Decoded Numbers

# Medium
# You are given an integer array nums.

# Each nums[i] is an encoded integer representing two positive integers xi and yi. To decode nums[i], define:

# widthi = nums[i] % 10.
# di = floor(nums[i] / 10).
# xi as the integer formed by the first widthi digits of the decimal representation of di.
# yi as the integer formed by all remaining digits of the decimal representation of di.
# It is guaranteed that the decimal representation of di contains more than widthi digits. Therefore, both xi and yi contain at least one digit.

# The decoded value of nums[i] is xiyi.

# Return the sum of the decoded values of all elements in nums, modulo 109 + 7.

# The floor() function returns the integer part of the division.

class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        ans = 0 
        for i in nums:
            width = i%10 
            d = i//10 
            s = str(d)
            x = int(s[:width])
            y = int(s[width:])
            ans = (ans+pow(x,y,10**9+7))%(10**9+7)
        return ans
