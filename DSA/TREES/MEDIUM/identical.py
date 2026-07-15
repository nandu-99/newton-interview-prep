# Check if two trees are identical

# Problem Statement: Given two Binary Trees, return if true if the two trees are identical, otherwise return false..

# Two trees are said to be identical if these three conditions are met for every pair of nodes :

# Value of a node in the first tree is equal to the value of the corresponding node in the second tree.
# Left subtree of this node is identical to the left subtree of the corresponding node.
# Right subtree of this node is identical to the right subtree of the corresponding node.

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

def identical(root1, root2):
    if not root1 and not root2:
        return True 
    if not root1 or not root2:
        return False 
    return (root1.val == root2.val) and identical(root1.left, root2.left) and identical(root1.right, root2.right)

print(identical(a, b))
