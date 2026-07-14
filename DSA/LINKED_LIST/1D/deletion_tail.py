# Delete node at the end of the Linked List 

# Implement the deleteAtTail function that allows the deletion at the end of the Linked List.

class Node:
    def __init__(self, x):
        self.data = x 
        self.next = None

def deleteAtTail(head):
    temp = head 
    while temp.next.next:
        temp = temp.next 
    temp.next = None 
    return head 

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

new = deleteAtTail(a)

printLL(new)
