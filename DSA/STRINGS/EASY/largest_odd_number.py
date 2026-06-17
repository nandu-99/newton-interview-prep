# Largest Odd Number in a String.

# Problem Statement: Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
# The number returned should not have leading zero's. But the given input string may have leading zero

# Example 1
# Input: s = "5347"
# Output: "5347"
# Explanation: The odd numbers formed by the given string are → 5, 3, 53, 347, 5347. The largest odd number without leading zeroes is 5347


s = input()

def largest_odd_number(s):
    ind = -1 
    for i in range(len(s)-1, -1, -1):
        if int(s[i])%2==1:
            ind = i 
            break 
    
    i = 0 
    while i<=ind and s[i]=='0':
        i+=1 
    return s[i:ind+1]

print(largest_odd_number(s))
