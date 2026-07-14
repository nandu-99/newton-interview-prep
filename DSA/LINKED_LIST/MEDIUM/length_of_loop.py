# Length of Loop in Linked List

# Problem Statement: Given the head of a linked list, determine the length of a loop present in the linked list. If there's no loop present, return 0.


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

def calc(meet):
    temp = meet 
    count = 1 
    while temp.next!=meet:
        count+=1 
        temp = temp.next 
    return count

def length_of_loop(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow==fast:
            return calc(slow)
    return 0 

print(length_of_loop(a))
