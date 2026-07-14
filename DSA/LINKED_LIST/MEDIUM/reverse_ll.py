# Reverse a Linked List

# Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.

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

def reverse(head):
    prev = None 
    temp = head 
    while temp:
        nex = temp.next 
        temp.next = prev 
        prev = temp 
        temp = nex 
    return prev 

k = reverse(a)

printLL(k)
