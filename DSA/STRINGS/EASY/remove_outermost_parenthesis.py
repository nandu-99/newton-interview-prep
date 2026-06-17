# Remove Outermost Parentheses
# Problem Statement: A valid parentheses string is defined by the following rules:

# It is the empty string "".
# If A is a valid parentheses string, then so is "(" + A + ")".
# If A and B are valid parentheses strings, then A + B is also valid.

# A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.

# Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return the resulting string.

# Example 1:
# Input:
#  s = "((()))"
# Output:
#  "(())"
# Explanation:
#  The input string is a single primitive: "((()))".  
# Removing the outermost layer yields: "(())".

s = input()

def remove_outermost(s):
    res = ""
    count = 0 
    for i in s:
        if i=="(":
            if(count>0):
                res+=i 
            count+=1 
        elif i==")":
            count-=1
            if count>0:
                res+=i 
    return res  

print(remove_outermost(s))
