# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode):
        ans = []
        def levelSearch(root):
            if not root:
                return
            curr = [root]
            while curr:
                ans_each = []
                temp = []
                for i in curr:
                    ans_each.append(i.val)
                    if i.left:
                        temp.append(i.left)
                    if i.right:
                        temp.append(i.right)
                ans.append(sum(ans_each) / len(ans_each))
                curr = temp
            return ans
        levelSearch(root)







