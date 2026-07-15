# Zig Zag Traversal Of Binary Tree

# Problem Statement: Given a Binary Tree, print the zigzag traversal of the Binary Tree. Zigzag traversal of a binary tree is a way of visiting the nodes of the tree in a zigzag pattern, alternating between left-to-right and right-to-left at each level.

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

def zigzag(root):
    ans = []
    q = deque([root])
    i = 0
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if i%2==0:
            ans.append(level)
        else:
            ans.append(level[::-1])
    return ans 

print(zigzag(a))
