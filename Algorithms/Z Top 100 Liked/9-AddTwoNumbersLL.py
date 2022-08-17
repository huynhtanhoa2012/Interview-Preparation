# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        l3 = dummy_head
        carry = 0
        current_sum = 0
        while l1 or l2:
            # get l1 and l2 value
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            # calculate current sumi
            current_sum = l1_val + l2_val + carry
            carry = current_sum//10
            digit = current_sum%10
            # add digit into l3 link list
            new_node = ListNode(digit)
            l3.next = new_node
            # Shift all l1,l2
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            l3 = l3.next

        # in case carry > 0
        if carry > 0:
            new_node = ListNode(carry)
            l3.next = new_node
            l3 = l3.next
        return dummy_head.next




