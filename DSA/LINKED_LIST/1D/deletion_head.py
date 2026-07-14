# Delete node at the beginning of the Linked List

# Implement the deleteAtHead function that allows the deletion of the head of the Linked List.

# Input:
# 4
# 5 10 15 20
# Output:
# 10 15 20

class Node:
    def __init__(self, x):
        self.data = x 
        self.next = None 
    

def deleteAtHead(head):
    if head is None or head.next is None: return None 
    head = head.next 
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

a.next = b 
b.next = c 
c.next = d 

new = deleteAtHead(a)

printLL(new)
