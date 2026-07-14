# Insert node at the end of the Linked List

# Implement InsertAtTail function that allows insertion of elements at the end of the Linked List.

# Input:
# 4
# 5 10 15 20
# 15
# Output:
# 5 10 15 20 15

class Node:
    def __init__(self, x):
        self.data = x 
        self.next = None

def InsertAtTail(head, value):
    new = Node(value)
    if not head:
        return new 
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new 
    return head 

def printLL(head):
    temp = head 
    while temp:
        print(temp.data, end=" ")
        temp = temp.next 
    

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

a.next = b 
b.next = c 
c.next= d 
d.next = e 

InsertAtTail(a, 60)

printLL(a)
