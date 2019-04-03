# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.ans = []
        self.preOrder(root)
        for i in range(len(self.ans)):
            if k - self.ans[i] in self.ans[i:]:
                return True
        return False
    def preOrder(self, root):
        if not root:
            return
        self.ans.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
