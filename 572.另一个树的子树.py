# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.subTree(s, t):
            return True
        self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def subTree(self,s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        elif s.val != t.val:
            return False
        else:
            return self.subTree(s.left, t.left) and self.subTree(s.right, t.right)

