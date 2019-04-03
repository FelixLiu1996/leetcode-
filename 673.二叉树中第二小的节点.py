# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = [root.val]
        self.search(root)
        if len(self.ans) >= 2:
            self.ans.sort()
            return self.ans[1]
        else:
            return -1

    def search(self, root):
        if not root:
            return None
        if root.val > self.ans[0]:
            self.ans.append(root.val)
        self.search(root.left)
        self.search(root.right)