# Recursive Implementation of atoi()

# Problem Statement: Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer (similar to the C/C++ atoi function).

# Steps to Implement: 1. First, ignore any leading whitespace characters ' ' until the first non-whitespace character is found.
# 2. Check the next character to determine the sign. If it’s a '-', the number should be negative. If it’s a '+', the number should be positive. If neither is found, assume the number is positive.
# 3. Read the digits and convert them into a number. Stop reading once a non-digit character is encountered or the end of the string is reached. Leading zeros should be ignored during conversion.
# 4. The result should be clamped within the 32-bit signed integer range: [-2147483648, 2147483647]. If the computed number is outside this range, return -2147483648 if the number is less than -2147483648, or return 2147483647 if the number is greater than 2147483647.
# 5. Finally, return the computed number after applying all the above steps.

# Example 1:
# Input:
#  s = " -12345"  
# Output:
#  -12345  

s = input()

def helper(s, i, num, sign):
    if i>=len(s) or not s[i].isdigit():
        return num*sign 
    
    num = num*10+int(s[i])

    if sign*num<=-2**31: return -2**31 
    if sign*num>=2**31-1: return 2**31-1 

    return helper(s, i+1, num, sign)

def atoi(s):
    i = 0 
    while i<len(s) and s[i]==' ':
        i+=1 
    
    sign = 1
    if i<len(s) and (s[i]=='+' or s[i]=='-'):
        sign = -1 if s[i]=='-' else 1 
        i+=1 
    return helper(s, i, 0, sign)


print(atoi(s))
