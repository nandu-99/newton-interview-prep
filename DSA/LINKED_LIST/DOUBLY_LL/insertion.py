# Insert at end of Doubly Linked List

# Problem Statement: Given a doubly linked list, and a value ‘k’, insert a node having value ‘k’ at the end of the doubly linked list.

# Example 1:
# Input Format:
  
# DLL: 1 <-> 2 <-> 3 <-> 4  
# Value to be Inserted: 6  
# Result:
#   DLL: 1 <-> 2 <-> 3 <-> 4 <-> 6  


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

def insertion(head, val):
    new = Node(val)
    temp = head 
    while temp.next:
        temp = temp.next  
    temp.next = new 
    new.prev = temp 
    return head 

k = insertion(a, 60)
printLL(k)
