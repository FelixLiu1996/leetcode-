# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if abs(self.layer(root.left) - self.layer(root.right)) <= 1:
            """还得判断子树是否是平衡的"""
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    def layer(self, root):
        if root:
            return max(self.layer(root.left), self.layer(root.right)) + 1
        else:
            return 0
x = Solution()
