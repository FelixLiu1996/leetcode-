class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 修剪较长的链表
        # 在等长的情况下判断是否有相交
        len1, len2 = 0, 0
        curr1, curr2 = headA, headB
        while curr1:
            len1 += 1
            curr1 = curr1.next
        while curr2:
            len2 += 1
            curr2 = curr2.next
        if len1 > len2:
            cut = len1 - len2
            while cut > 0:
                headA = headA.next
                cut -= 1
        elif len1 < len2:
            cut = len2 - len1
            while cut > 0:
                headB = headB.next
                cut -= 1
        temp1, temp2 = headA, headB
        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1

        # 下面这样不行
        # while temp1:
        #     if temp1.val == temp2.val:
        #         break
        #     else:
        #         temp1 = temp1.next
        #         temp2 = temp2.next
        # return temp1

