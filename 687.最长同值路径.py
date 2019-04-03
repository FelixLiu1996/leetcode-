# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        self.search(root)
        return self.ans

    def search(self, root):
        if not root:
            return 0
        left_long = self.search(root.left)
        right_long = self.search(root.right)
        left, right = 0, 0
        if root.left and root.left.val == root.val:
            left = left_long + 1
        if root.right and root.right.val == root.val:
            right = right_long + 1
        self.ans = max(self.ans, left + right)
        return max(left, right)


