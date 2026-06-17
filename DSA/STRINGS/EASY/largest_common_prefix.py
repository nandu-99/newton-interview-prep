# Longest Common Prefix
# Problem Statement: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

# Example 1
# Input: str = ["flower", "flow", "flight"]
# Output: "fl"
# Explanation: All strings in the array begin with the common prefix "fl".

arr = list(map(str, input().split(", ")))

def longest_common_prefix(arr):
    ans = ""
    arr.sort()
    first = arr[0]
    last = arr[-1]
    for i in range(min(len(first), len(last))):
        if first[i]!=last[i]:
            return ans 
        ans+=first[i]
    return ans 

print(longest_common_prefix(arr))
