# 4034. Minimum Bishop Moves to Reach Target

# Medium


# There is an 8 x 8 empty chessboard with 1-indexed rows and columns.

# You are given an array source = [sr, sc] representing the starting position of a bishop, and an array target = [tr, tc] representing the target position.

# In one move, the bishop travels one or more squares along a single diagonal direction, staying within the board.

# Return the minimum number of moves for the bishop to land exactly on target. If it can never reach target, return -1.


# Example 1:

# Input: source = [8,1], target = [1,8]

# Output: 1

def minBishopMoves(self, source: list[int], target: list[int]) -> int:
    sc_color = sum(source)%2 
    tc_color = sum(target)%2 
    if source==target:
        return 0 
    elif sc_color!=tc_color:
        return -1 
    # print(source[0]-source[1], target[0]-target[1])
    if abs(source[0]-target[0])==abs(source[1]-target[1]):
        return 1
    else:
        return 2 
            