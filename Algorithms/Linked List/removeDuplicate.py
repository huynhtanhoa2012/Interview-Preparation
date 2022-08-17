# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def removeDuplicates(head: ListNode) -> ListNode:

    current = head
    while current:
        # compare 2 adjacency nodes
        while current.next and current.val == current.next.val:
            # delete node
            current.next = current.next.next
        # shift current 
        current = current.next


    return None