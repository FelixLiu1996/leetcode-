# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        self.ans = []
        self.preOrder(t)
        return ''.join(self.ans)
    def preOrder(self, root):
        if not root:
            return
        self.ans.append(str(root.val))
        if root.left:
            self.ans.append('(')
            self.preOrder(root.left)
            self.ans.append(')')
        if root.right:
            #如果左子树没有，需要增加一个括号
            if not root.left:
                self.ans.append('()')
            self.ans.append('(')
            self.preOrder(root.right)
            self.ans.append(')')
