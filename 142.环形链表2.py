class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 寻找环的第一个节点的方法是：
        # 首先假定链表起点到入环的第一个节点A的长度为a【未知】
        # 到快慢指针相遇的节点B的长度为（a + b）【这个长度是已知的】。
        # 现在我们想知道a的值，注意到快指针p2始终是慢指针p走过长度的2倍，所以慢指针p从B继续走（a + b）又能回到B点
        # 如果只走a个长度就能回到节点A
        # 所以通过一个指针从头节点出发，每次走一步，同时慢指针从当前位置出发，当相遇时，则是环的第一个节点
        slow = fast = head
        flag = False

        # 若有环则在第一次相遇时停止
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break

        # 如果存在环形
        if flag:
            temp = head
            while temp != slow:
                slow = slow.next
                temp = temp.next
            return slow
        # 如果不存在环形
        else:
            return None


