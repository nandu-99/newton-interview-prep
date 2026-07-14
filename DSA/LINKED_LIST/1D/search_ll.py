# Search an element in a Linked List

# Problem Statement: Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.

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

def search(head, val):
    temp = head 
    while temp:
        if temp.data == val:
            return True 
        temp = temp.next 
    return False 

print(search(a, 30))
