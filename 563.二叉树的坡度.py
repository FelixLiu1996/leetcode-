# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0  #记录坡度
        self.preOrder(root)
        return self.ans

    def preOrder(self, root):
        if not root:
            return 0
        left_sum = root.left.val + self.preOrder(root.left) if root.left else self.preOrder(root.left)
        right_sum = root.right.val + self.preOrder(root.right) if root.right else self.preOrder(root.right)
        self.ans += abs(left_sum - right_sum)
        return left_sum + right_sum



