# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            if root.left and root.right:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            elif root.left is not None:
                return self.minDepth(root.left) + 1
            elif root.right is not None:
                return self.minDepth(root.right) + 1
            else:
                return 1
        else:
            return 0

