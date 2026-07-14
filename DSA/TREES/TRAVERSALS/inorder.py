# Inorder Traversal of Binary Tree

# Problem Statement: Given root of binary tree, return the Inorder traversal of the binary tree.

# Example 1:
# Input:
#  root = [1, 4, null, 4, 2]  
# Output:
#  [4, 4, 2, 1]  
# Explanation:
#  In this example, the preorder traversal of the binary tree produces the sequence [4, 4, 2, 1].


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

def inorder(root):
    def helper(root, curr=[]):
        if not root:return None 
        helper(root.left, curr)
        curr.append(root.val)
        helper(root.right, curr)
        return curr 
    return helper(root)

print(inorder(a))
