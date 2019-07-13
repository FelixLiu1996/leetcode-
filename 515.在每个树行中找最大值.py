#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        ans = [root.val]
        curr = [root]

        while len(curr):
            temp_queue = []
            #temp_ans = float('-inf')
            temp_ans = -10000000000
            for i in curr:
                if i.val > temp_ans:
                    temp_ans = i.val
                if i.left:
                    temp_queue.append(i.left)
                if i.right:
                    temp_queue.append(i.right)
            curr = temp_queue
            ans.append(temp_ans)
        return ans
