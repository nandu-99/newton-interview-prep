# Check if one string is rotation of another

# Problem Statement: Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position. For example, if s = "abcde", then it will be "bcdea" after one shift.

# Example 1:
# Input:
#  s = "rotation", goal = "tionrota"
# Output:
#  true
# Explanation:
#  After multiple left shifts on "rotation", we get:
#     1st shift → "otationr"
#     2nd shift → "tationro"
#     3rd shift → "ationrot"
#     4th shift → "tionrota"
#     So the goal string can be obtained by rotating the original string.

s = input()
g = input()

def rotation(s, g):
    if len(s)!=len(g):
        return False 
    double = s+s 
    if g in double:
        return True 
    else: return False

print(rotation(s, g))
