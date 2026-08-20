# Maximum sum of non-adjacent elements (DP 5)

# Problem Statement: Given an array of N positive integers, we need to return the maximum sum of the subsequence such that no two elements of the subsequence are adjacent elements in the array.

# Note: A subsequence of an array is a list with elements of the array where some elements are deleted (or not deleted at all) and the elements should be in the same order in the subsequence as in the array.

# Input: nums = [1, 2, 4]
# Output: 5
# Explanation: 
# Subsequence {1,4} gives maximum sum.

def max_sum_non_adjacent(arr):
    d = {}
    def recur(i):
        if i in d:return d[i]
        if i>=len(arr):return 0 
        one = recur(i+2)+arr[i]
        two = recur(i+1)
        d[i] = max(one, two)
        return d[i]
    return recur(0)

print(max_sum_non_adjacent([1, 2, 4]))
