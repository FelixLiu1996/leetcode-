# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # # 复杂的笨办法
        # # 把两个链表的数值取出来相加
        # # 再放到新的链表中去，返回新链表
        # stack1 = []
        # stack2 = []
        # temp1 = l1
        # temp2 = l2
        # # 因为是逆序存储
        # # 所以分别将两个链表的值压入栈中
        # while temp1:
        #     stack1.append(temp1.val)
        #     temp1 = temp1.next
        # while temp2:
        #     stack2.append(temp2.val)
        #     temp2 = temp2.next
        # # 分别将栈中元素弹出，并转化成十进制数
        # num1, num2 = 0, 0
        # while stack1:
        #     temp_num = stack1.pop()
        #     num1 = num1 * 10 + temp_num
        # while stack2:
        #     temp_num = stack2.pop()
        #     num2 = num2 * 10 + temp_num
        # ans_num = num1 + num2
        # # 将结果表示的数按位压入栈中
        # stack = []
        # if ans_num == 0:
        #     return ListNode(0)
        # while ans_num > 0:
        #     stack.append(ans_num % 10)
        #     ans_num //= 10
        # # 将栈中元素逆序放到链表中
        # l3 = ListNode(None)
        # curr = l3
        # while stack:
        #     temp_num = stack.pop(0)
        #     curr.next = ListNode(temp_num)
        #     curr = curr.next
        # return l3.next

        # 正常的解法
        # 链表相应位置数值相加，若超过10，则有进位
        curr1 = l1
        curr2 = l2
        l3 = ListNode(None)
        temp = l3
        carry = 0  # 进位
        while curr1 or curr2:
            num1 = curr1.val if curr1 else 0
            num2 = curr2.val if curr2 else 0
            sum = num1 + num2 + carry
            carry = sum // 10   # 将进位放到下一个迭代过程计算
            temp.next = ListNode(sum % 10)
            temp = temp.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if carry:
            temp.next = ListNode(carry)
        return l3.next


