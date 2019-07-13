# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(None)
        temp.next = head
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return temp.next












#         pre = ListNode(None)
#         pre.next = head
#         if not head:
#             return []
#         curr = pre.next
#         while curr:
#             if curr.val == val:
#                 curr = curr.next
#                 pre.next = curr
#             else:
#                 curr = curr.next
#                 pre = pre.next
        #return pre.next

