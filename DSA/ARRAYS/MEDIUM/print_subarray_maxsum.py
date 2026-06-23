# follow up of kadane's algo 

#print the subarray with max sum 

# Example 1:
# Input: nums = [2, 3, 5, -2, 7, -4]  
# Output: [2, 3, 5, -2, 7]

arr = list(map(int, input().split()))

def print_subarray(arr):
    maxi = float('-inf') 
    start = 0
    summ = 0 
    ansstart = -1 
    ansend = -1 
    for i in range(len(arr)):
        if summ==0:
            start = i 
        summ+=arr[i]
        if summ>maxi:
            maxi = summ 
            ansstart = start 
            ansend = i 
        if summ<0:
            summ = 0 
    print("[", end=" ")
    for i in range(ansstart, ansend+1):
        
        print(arr[i], end=" ")
    print("]")
    return maxi 

print(print_subarray(arr))
