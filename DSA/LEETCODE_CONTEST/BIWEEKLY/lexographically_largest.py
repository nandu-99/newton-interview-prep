# 4036. Lexicographically Largest String After Pair Transformations

# Medium

# You are given an integer array nums.

# For each integer x in nums, start with a string consisting of exactly x lowercase 'a' characters.

# You may perform the following operation any number of times (including zero):

# Choose two adjacent equal letters and replace them with the next letter in the alphabet.
# For example, "aa" can be replaced with "b", and "bb" can be replaced with "c". The pair "zz" cannot be replaced.

# For each x, determine the lexicographically largest string that can be obtained.

# Return an array of strings where the ith string is the answer for nums[i].

# A string a is lexicographically larger than a string b if, at the first position where they differ, a contains a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters are equal, the longer string is lexicographically larger.

class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        ans = []
        # nums = [2**26+1]
        for i in nums:
            l = 0 
            k = []
            while i>0:
                if l==25:
                    k.append('z'*i)
                    break
                if i%2==1:
                    k.append((chr(ord('a')+l)))
                i//=2 
                l+=1
            ans.append(''.join(k[::-1]))
        return ans
                    