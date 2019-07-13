# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        # 迭代方式
        if not root:
            return []
        ans = []
        curr = [root]
        zigzag_count = 0  # 通过这个进行奇偶反转
        while len(curr):
            ans_each = []
            temp = []
            for i in curr:
                ans_each.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if zigzag_count % 2 != 0:
                ans.append(ans_each[::-1])
            else:
                ans.append(ans_each)
            zigzag_count += 1
            curr = temp
        return ans
