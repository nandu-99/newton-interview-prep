# Check if the given Linked List is Palindrome


# Problem Statement: Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. Check whether the linked list values form a palindrome or not. Return true if it forms a palindrome, otherwise, return false. .

# A palindrome is a sequence that reads the same forward and backwards.

# Example 1:
# Input: head -> 3 -> 7 -> 5 -> 7 -> 3
# Output: true
# Explanation: 37573 is a palindrome.

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
c = Node(2)
d = Node(1)
# e = Node(1)
# f = Node(1)

a.next = b 
b.next = c 
c.next = d 

def reverse(head):
    prv = None 
    temp = head 
    while temp:
        nex = temp.next 
        temp.next = prv 
        prv = temp 
        temp = nex 
    return prv

def ispalindrome(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    
    middle = slow 
    sechead = reverse(middle)

    first = head 
    second = sechead 

    while second:
        if first.data!=second.data:
            return False 
        first = first.next 
        second =second.next 
    return True 

print(ispalindrome(a))
