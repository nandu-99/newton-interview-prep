# Maximum depth of a Binary Tree

# Problem Statement:
# Given the root of a Binary Tree, return the height of the tree. The height of the tree is equal to the number of nodes on the longest path from root to a leaf.



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

def maximum_depth(root):
    level = 0 
    if not root:return level 
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level+=1 
    return level 

print(maximum_depth(a))
