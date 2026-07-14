# Delete Last Node of a Doubly Linked List

# Problem Statement: Given a Doubly Linked List, delete the last node of the Doubly Linked List.

class Node:
    def __init__(self, x):
        self.data = x 
        self.next = None 
        self.prev = None

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
b.prev = a
b.next = c 
c.prev = b
c.next = d 
d.prev = c  

def deletion(head): 
    if head is None or head.next is None:return None 
    temp = head 
    while temp.next.next:
        temp = temp.next 
    temp.next = None  
    return head  

k = deletion(a)
printLL(k)
    