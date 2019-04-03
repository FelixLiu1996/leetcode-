# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node'):
        # 迭代法
        stack = [root]
        ans = []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.children:
                temp.children.reverse()
                stack.extend(temp.children)
        return ans[::-1]

