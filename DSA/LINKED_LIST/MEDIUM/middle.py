# Find middle element in a Linked List

# Problem Statement: Given the head of a linked list of integers, determine the middle node of the linked list. However, if the linked list has an even number of nodes, return the second middle node.

class Node:
    def __init__(self, x):
        self.data = x 
        self.next = None 

def printLL(head):
    temp = head 
    while temp:
        print(temp.data)
        temp = temp.next

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b 
b.next = c 
c.next = d 

def middle(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        
        fast = fast.next.next 
        slow = slow.next 
    return slow.data 

printLL(a)
print(middle(a))
