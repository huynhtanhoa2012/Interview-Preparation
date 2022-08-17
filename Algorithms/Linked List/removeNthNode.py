# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthNodeFromEnd(head: ListNode, n: int) -> ListNode:
    
    # create dummy node to store linked list
    dummy = ListNode(0, head)
    left = dummy.next
    right = head
    len

    # shift right 
    while n > 0 and right:
        right = right.next

    # shift both left and right
    while right:
        left = left.next
        right = right.next
    left = left.next.next

    return dummy.next

    