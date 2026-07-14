# Insert node at the beginning of the Linked List

# Implement InsertAtHead function that allows insertion of elements at the beginning of the Linked List.

# Input:
# 4
# 5 10 15 20
# 15
# Output:
# 15 5 10 15 20

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
    

def InsertAtHead(head, value):
    new = Node(value)
    new.next = head 
    head = new 
    return head 



new = InsertAtHead(a, 50)

printLL(new)
