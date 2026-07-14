# Starting point of loop in a Linked List

# Problem Statement: Given the head of a linked list that may contain a cycle, return the starting point of that cycle. If there is no cycle in the linked list return null.

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

def detect_starting(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow==fast:
            slow = head 
            while slow!=fast:
                slow= slow.next 
                fast = fast.next 
            return slow.data
    return None


print(detect_starting(a))
