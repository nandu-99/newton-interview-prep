# Segregate even and odd nodes in LinkedList

# Problem Statement: Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list. Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.

class Node:
    def __init__(self, x):
        self.data = x 
        self.next = None 

def printLL(head):
    temp = head 
    while temp:
        print(temp.data)
        temp = temp.next

a = Node(1)
b = Node(2)
c = Node(4)
d = Node(3)

a.next = b 
b.next = c 
c.next = d 

def evenodd(head):
    evenhead = Node(0) 
    oddhead = Node(0) 
    
    temp = head 
    tempeven = evenhead 
    tempodd = oddhead

    while temp:
        if temp.data%2==0:
            tempeven.next = temp 
            tempeven = tempeven.next
        else:
            tempodd.next = temp 
            tempodd = tempodd.next 
        temp = temp.next 
    
    if not evenhead.next:
        return oddhead.next 
    
    if not oddhead.next:
        return evenhead.next 
    
    tempeven.next = oddhead.next 
    return evenhead.next
    

k = evenodd(a)
printLL(k)
