class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 通过计数然后得到
        count = 0
        temp1 = head
        temp2 = head
        while temp1:
            count += 1
            temp1 = temp1.next
        count //= 2
        while count >= 0:
            temp2 = temp2.next
            count -= 1
        return temp2
        # 快慢指针法
        # p1 = head
        # p2 = head
        #
        # while (p2 and p2.next):
        #     p1 = p1.next
        #     p2 = p2.next.next
        # return p1