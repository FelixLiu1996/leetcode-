# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        result = []
        s = ''
        if root is None:
            return result
        else:
            self.searchPath(root, result, s)
            return result

    def searchPath(self, root, result, s):
        """判断是否是根节点出发还没有进入子节点"""
        if len(s) != 0:
            s = s + '->' + str(root.val)
        else:
            s = str(root.val)
        if root.left:
            self.searchPath(root.left, result, s)
        if root.right:
            self.searchPath(root.right, result, s)
        if root.left is None and root.right is None:
            """表明此节点已经达到叶节点"""
            result.append(s)
            return
