# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode):
        self.changeChildTree(root)
        return root

    def changeChildTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.changeChildTree(root.left)
            self.changeChildTree(root.right)
            return root
        else:
            return root
