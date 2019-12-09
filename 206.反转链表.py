  # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 自己的做法
        # stack = []
        # curr = head
        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        # curr = head
        # while curr:
        #     temp = stack.pop()
        #     curr.val = temp
        #     curr = curr.next
        # return head

        # 高级做法
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev




