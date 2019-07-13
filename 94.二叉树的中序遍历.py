# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归方法很容易
    # def inorderTraversal(self, root: TreeNode):
    #     self.ans = []
    #     self.inorder(root)
    #
    # def inorder(self, root):
    #     if not root:
    #         return
    #     self.inorder(root.left)
    #     self.ans.append(root)
    #     self.inorder(root.right)

    # 迭代算法
    def inorderTraversal(self, root: TreeNode):
        stack = []
        ans = []
        while (stack or root):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
