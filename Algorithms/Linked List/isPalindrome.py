#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome( head: ListNode) -> int:

    slow, fast = head, head
    
    # 1. find middle element
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # 2. reverse second half => prev = last node
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # 3. check palindrome
    left , right = head, prev

    while right: # last node of right point to Null
        if left.val != right.val:
            return 0
        left = left.next
        right = right.next
    return 1