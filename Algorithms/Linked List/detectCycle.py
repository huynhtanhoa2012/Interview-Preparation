

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True

    return False

ls = ['k',"df",231]