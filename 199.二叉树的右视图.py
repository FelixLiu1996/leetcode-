# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return None
        curr = [root]
        ans = []
        while curr:
            temp = []
            ans.append(curr[-1].val)
            for i in curr:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            curr = temp
        return ans