# Implement Pow(x,n) | X raised to the power N

# Problem Statement: Implement the power function pow(x, n) , which calculates the x raised to n i.e. xn.

# Example 1:
# Input:
#  x = 2.0000, n = 10  
# Output:
#  1024.0000  
# Explanation:
#  The answer is calculated as 2^10, which equals 1024.

x = float(input())
n = int(input())

def helper(x, n):
    if n==0:
        return 1.0 
    if n==1: 
        return x 
    
    if n%2==0:
        return helper(x*x, n//2)
    else:
        return x*helper(x, n-1)

def power(x, n):
    if n<0:
        return 1/helper(x, -n)
    return helper(x, n)

print(power(x, n))
