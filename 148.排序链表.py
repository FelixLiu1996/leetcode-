# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        return self.sortMerge(head)

    def sortMerge(self, head):
        if not head.next:
            return head
        # 慢指针和快指针，快指针每次跳动两个元素，慢指针每次往后挪一个
        # 这样当快指针到达到链表最后的时候，慢指针在中间位置
        fast_pointer, slow_pointer = head, head
        pre = None
        while fast_pointer and fast_pointer.next:
            pre = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        pre.next = None #  必须得截断 不然就不是两个子链表
        left = self.sortMerge(head)
        right = self.sortMerge(slow_pointer)
        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.val < right.val:
            res = left
            res.next = self.merge(left.next, right)
        else:
            res = right
            res.next = self.merge(left, right.next)
        return res
