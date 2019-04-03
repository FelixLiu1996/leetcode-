# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        #  这样做不可以 待研究
        # if L <= root.val <= R:
        #     self.trimBST(root.left, L, R)
        #     self.trimBST(root.right, L, R)
        # if root.val < L:
        #     root = root.right
        #     self.trimBST(root, L, R)
        # if root.val > R:
        #     root = root.left
        #     self.trimBST(root, L, R)
        # return root
        def trim(root):
            if not root:
                return None
            if L <= root.val <= R:
                root.left = trim(root.left)
                root.right = trim(root.right)
                return root
            elif root.val > R:
                return trim(root.left)
            elif root.val < L:
                return trim(root.right)
        return trim(root)