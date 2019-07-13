# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        curr = l3
        while l1 is not None and l2 is not None:
            if l2.val < l1.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
        if l1 is not None:
            curr.next = l1
        if l2 is not None:
            curr.next = l2
        return l3.next
