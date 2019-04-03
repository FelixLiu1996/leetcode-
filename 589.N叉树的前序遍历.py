# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node'):
     #  迭代法
        stack = [root]
        ans = []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.children:
                temp.children.reverse()
                stack.extend(temp.children)
        return ans

    #   用的递归法
    #     self.ans = []
    #     self.order(root)
    #     return self.ans
    #
    # def order(self, root):
    #     if not root:
    #         return None
    #     self.ans.append(root.val)
    #     for child in root.children:
    #         self.order(child)





