class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        # if not head:
        #     return None
        # pre = head
        # length = 0
        # while pre.next:
        #     length += 1
        #     pre = pre.next
        # position = length - n - 1
        # post = head
        # while position > 0:
        #     post = post.next
        #     position -= 1
        # if n == length:
        #     head = head.next
        # else:
        #     if post.next:
        #         post.next = post.next.next
        # return head

        # 添加一个哑变量解决特殊条件，如头结点或只有一个元素问题等等
        # dummy = ListNode(0)
        # dummy.next = head
        # pre = head
        # length = 0
        # while pre:
        #     length += 1
        #     pre = pre.next
        # position = length - n
        # post = dummy
        # while position > 0:
        #     post = post.next
        #     position -= 1
        # post.next = post.next.next
        # return dummy.next

        # 以上均用到了两次遍历，下面一次遍历方法
        dummy = ListNode(0)
        dummy.next = head
        # 使用快慢指针，快指针先走n步，然后快慢指针同时走，当快指针到达最后节点时，慢节点到达倒数n+1节点
        fast = head
        while n:
            fast = fast.next
            n -=1
        slow = dummy
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next