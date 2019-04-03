# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.childIsSymmetric(root.left, root.right)

    def childIsSymmetric(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is None:
            return False
        elif left is None and right is not None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.childIsSymmetric(left.left, right.right) and self.childIsSymmetric(left.right, right.left)

