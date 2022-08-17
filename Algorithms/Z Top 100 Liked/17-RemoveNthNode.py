class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 1: find index of node before removed node
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
       
    # find length of link list
    current = head
    length = 0
    while current:
        current = current.next
        length += 1

    # edge case, remove first node, there is no node before first node
    if length == n:
        return head.next

    # find index of node before the node to remove
    index = length - n - 1
    current = head
    for i in range(index):
        current = current.next
    
    current.next = current.next.next
    return head

# Approach 2: Using 2 pointers
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    
    # 1. move current node n steps into list
    current = head
    for i in range(n):
        current = current.next

    # edge case if n reach the end that means the node need to remove 
    # is the first node
    if not current:
        return head.next  # return second node

    # 2. move both pointers until currentNode reaches to the end
    nodeBeforeRemoved = head
    while current.next:
        current = current.next
        nodeBeforeRemoved = nodeBeforeRemoved.next
    
    nodeBeforeRemoved.next = nodeBeforeRemoved.next.next

    return head 
