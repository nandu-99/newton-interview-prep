# Preorder Traversal of Binary Tree

# Problem Statement: Given the root of a Binary Tree, return the preorder, inorder and postorder traversal sequence of the given tree by making just one traversal.

# Input: Binary Tree: 4 2 5 3 -1 7 6 -1 9 -1 -1 8 -1 1
# Output: Preorder: [4, 2, 3, 9, 1, 5, 7, 6, 8] 

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


def preorder(root): 
    def helper(root, curr=[]):
        if not root:return None 
        curr.append(root.val)
        helper(root.left, curr)
        helper(root.right, curr)
        return curr 
    return helper(root)

print(preorder(a))
