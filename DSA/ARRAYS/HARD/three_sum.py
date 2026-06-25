# 3 Sum : Find triplets that add up to a zero

# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.


# Input:
#  nums = [-1,0,1,2,-1,-4]
# Output:
#  [[-1,-1,2],[-1,0,1]]
# Explanation:
#  Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

arr = list(map(int, input().split()))
def three_sum(arr, target):
    ans = []
    for i in range(len(arr)):
        d = {}
        for j in range(i+1, len(arr)):
            comp = target-arr[i]-arr[j]
            if comp in d:
                ans.append((arr[i], comp, arr[j]))
            d[arr[j]] = j 
    return ans 

print(three_sum(arr, 0))
