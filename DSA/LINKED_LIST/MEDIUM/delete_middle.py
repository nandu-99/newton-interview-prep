# Delete the Middle Node of the Linked List

# Problem Statement: Given the head of a linked list of integers, delete the middle node of the linked list and return the modified head. However, if the linked list has an even number of nodes, delete the second middle node.

class Node:
    def __init__(self, x):
        self.data = x 
        self.next = None 

def printLL(head):
    temp = head 
    while temp:
        print(temp.data)
        temp = temp.next

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b 
b.next = c 
c.next = d 
d.next = e

def delete_middle(head):
    slow = head 
    fast = head.next.next 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    slow.next = slow.next.next 
    return head 

k = delete_middle(a)
printLL(k)
