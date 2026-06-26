# Merge Overlapping Sub-intervals

# Problem Statement: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input : intervals=[[1,3],[2,6],[8,10],[15,18]]
# Output : [[1,6],[8,10],[15,18]]
# Explanation : Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6] intervals.

intervals=[[1,3],[2,6],[8,10],[15,18]]

def merge_intervals(intervals):
    ans = []
    for interval in intervals:
        if not ans or ans[-1][1]<interval[0]:
            ans.append(interval)
        else:
            if ans[-1][1]<interval[1]:
                ans[-1][1] = interval[1]
    return ans 

print(merge_intervals(intervals))
