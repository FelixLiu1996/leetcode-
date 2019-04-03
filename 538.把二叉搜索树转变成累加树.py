# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.inOrder(root)
        return root

        #二叉搜索树的中序遍历是一个递增的列
    def inOrder(self, root, preans = 0):
        if not root:
            return preans
        root.val += self.inOrder(root.right, preans)
        return self.inOrder(root.left, root.val)