# Check if the Binary Tree is Balanced Binary Tree

# Problem Statement: Given a Binary Tree, return true if it is a Balanced Binary Tree else return false. A Binary Tree is balanced if, for all nodes in the tree, the difference between left and right subtree height is not more than 1..

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

def dfsHeight(root):
    if not root:return 0 
    lefty = dfsHeight(root.left)
    if lefty==-1:
        return -1 
    righty = dfsHeight(root.right)
    if righty==-1:return -1 
    if abs(lefty-righty)>1: return -1 
    return max(lefty, righty)+1

def balanced(root):
    return dfsHeight(root)!=-1
