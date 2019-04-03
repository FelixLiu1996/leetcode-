# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        Len = len(nums)
        if Len == 0:
            return None
        """取中间值作为root，左边的作为左子树，右边的作为右子树"""
        mid = Len // 2
        tree = TreeNode(nums[mid])
        tree.left = self.sortedArrayToBST(nums[: mid])
        tree.right = self.sortedArrayToBST(nums[mid + 1:])
        return tree
x = Solution()
print(x.sortedArrayToBST([-10,-3,0,5,9]))


