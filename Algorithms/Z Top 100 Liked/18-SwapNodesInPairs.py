class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def swapPairs(head: ListNode) -> ListNode:
    
    current = head

    while current.next and current.next.next:
        temp = current.next.next
        current.next = current
        current = temp
    
    print(current)
    return current