# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.compare = root.val
        def search(root):
            if not root:
                return True
            if root.val != self.compare:
                return False
            return search(root.left) and search(root.right)
        search(root)

    #     self.flag = 1
    #     self.search(root)
    #     return self.flag == 1
    # def search(self, root):
    #     if not root:
    #         return
    #     if root.left:
    #         if root.left.val != root.val:
    #             self.flag = 0
    #         self.search(root.left)
    #     if root.right:
    #         if root.right.val != root.val:
    #             self.flag = 0
    #         self.search(root.right)


