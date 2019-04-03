#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode):
        self.dic = {}
        self.search(root)
        self.dic = sorted(self.dic.items(), key=lambda x: x[1], reverse=True)
        ans = [x[0] for x in self.dic if x[1] == self.dic[0][1]]
        return ans

    def search(self, root):
        if not root:
            return None
        if root.val in self.dic:
            self.dic[root.val] += 1
        else:
            self.dic[root.val] = 1
        if root.left:
            self.search(root.left)
        if root.right:
            self.search(root.right)



