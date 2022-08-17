class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head: ListNode) -> ListNode:
    current = head
    prev = None
    next = None

    while current:
        # 1. store next node into temp variable
        next = current.next
        # 2. point current next to previous
        current.next = prev
        # 3. shift current and previous
        prev = current
        current = next
    print(prev)
    return prev

reverseList([1,2,3,4,5])
    