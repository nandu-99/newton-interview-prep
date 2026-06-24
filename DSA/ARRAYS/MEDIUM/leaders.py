# Leaders in an Array

# Example 1:
# Input:
#  arr = [4, 7, 1, 0]  
# Output:
#  7 1 0  
# Explanation:
#  The rightmost element (0) is always a leader.  
# 7 and 1 are greater than the elements to their right, making them leaders as well.

arr = list(map(int, input().split()))

def leaders(arr):
    # ans = []
    # for i in range(len(arr)):
    #     is_leader = True 
    #     for j in range(i+1, len(arr)):
    #         if arr[j]>arr[i]:
    #             is_leader = False 
    #             break 
    #     if is_leader:
    #         ans.append(arr[i])
    # return ans 
    ans = []
    maxi = arr[-1]
    ans.append(arr[-1])
    for i in range(len(arr)-2, -1, -1):
        if arr[i]>maxi:
            maxi = arr[i]
            ans.append(arr[i])
    return ans

print(leaders(arr))
