# Iterative Postorder Traversal of Binary Tree Using 2 Stacks

# Problem Statement: Given the root of a Binary Tree, create a function that performs a postorder traversal using two stacks and returns an array containing the traversal sequence.


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

def postorder(root):
    def helper(root, curr=[]):
        if not root:return None 
        helper(root.left, curr)
        helper(root.right, curr)
        curr.append(root.val)
        return curr 
    return helper(root)

print(postorder(a))
