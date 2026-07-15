# Size, Min and max Depth of a Binary Tree

# For a given binary tree, find the size of the tree, maximum depth of the tree, and the minimum element in the tree.
# Note:
# Size of the Tree: The size of a binary tree is the total number of nodes present in the tree.
# maximum depth of the Tree:The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Minimum Element in the Tree: The minimum element in a binary tree is the smallest value present among all the elements/nodes in the tree

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

a = Node(4)
b = Node(2)
c = Node(3)
d = Node(9)
e = Node(1)
f = Node(5)
g = Node(7)
h = Node(8)
i = Node(6)

a.left = b 
b.left = c 
c.right = d 
d.left = e 
a.right = f 
f.left = g
f.right = i 
i.left = h  

from collections import deque 

def maxdepth(root):
    if not root:return 0 
    lefty = maxdepth(root.left)
    righty = maxdepth(root.right)
    return max(lefty, righty)+1 

def minElement(root):
    if not root:return float('inf')
    lefty = minElement(root.left)
    righty = minElement(root.right)
    return min(lefty, righty, root.val)

def size(root):
    if not root:return 0 
    lefty = size(root.left)
    righty = size(root.right)
    return lefty+righty+1 

print(maxdepth(a))
print(minElement(a))
print(size(a))

