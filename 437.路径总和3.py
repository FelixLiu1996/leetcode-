# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0
        self.preOrderSearch(root, sum)
        return self.ans

    def bfs(self,root, sum):
        """深度优先搜索"""
        if not root:
            return None
        if root.val == sum:
            self.ans += 1
        if root.left:
            self.bfs(root.left, sum - root.val)
        if root.right:
            self.bfs(root.right, sum - root.val)
    def preOrderSearch(self, root):
        if not root:
            return None
        self.bfs(root, sum)
        self.preOrderSearch(root.left, sum)
        self.preOrderSearch(root.right, sum)


