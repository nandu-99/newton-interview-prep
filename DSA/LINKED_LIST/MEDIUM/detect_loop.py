# Detect a Cycle in a Linked List

# Problem Statement: Given a Linked List, determine whether the linked list contains a cycle or not.


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
d.next = a

def detect(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow==fast:
            return True 
    return False 

print(detect(a))
