# # Find the Length of a Linked List

# Problem Statement: Given the head of a linked list, print the length of the linked list.

# Input: 0->1->2 
# Output: 3


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

def length_linked_list(head):
    temp = head 
    count = 0 
    while temp:
        count+=1 
        temp = temp.next 
    return count 

print(length_linked_list(a))
        
