# Remove N-th node from the end of a Linked List

# Problem Statement: Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.

# Input:  5->1->2, N=2
# Output: 5->2
# Explanation: The 2nd node from the end of the linked list is 1. Therefore, we get this result after removing 1 from the linked list.


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

def delete_kth(head, k):
    slow = head 
    fast = head 
    for i in range(k+1):
        fast = fast.next 
    while fast is not None:
        slow = slow.next 
        fast = fast.next 
    slow.next = slow.next.next 
    return head 

l = delete_kth(a, 3)

printLL(a)
