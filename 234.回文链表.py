class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        # 时间复杂度O(n), 空间复杂度O(n)
        # temp = head
        # stack = []
        # while temp:
        #     stack.append(temp.val)
        #     temp = temp.next
        # return stack == stack[::-1]


        # 时间复杂度O(n), 空间复杂度O(1)
        # 快慢指针法 慢指针到中间，然后反转剩下一半的链表
        if not head:
            return True
        slow = head
        fast = head
        while fast:  # 用 while fast and fast.next 还需要判断奇偶
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        # 将剩下的链表反转
        stack = []
        temp = slow
        while temp:
            stack.append(temp.val)
            temp = temp.next
        temp = slow
        while temp:
            num = stack.pop()
            temp.val = num
            temp = temp.next
        curr = head
        while slow:
            if curr.val == slow.val:
                curr = curr.next
                slow = slow.next
            else:
                return False
        return True



