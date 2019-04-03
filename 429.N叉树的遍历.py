
#Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node):
        if not root:
            return []
        curr = [[root]]
        ans = []
        while curr:
            ans_each = []
            temp = []
            for i in curr:
                for j in i:
                    ans_each.append(j.val)
                    if j.children:
                        temp.append(j.children)
                #ans_each.append(i.val)
                #if i.children:
                    # for j in i.children:
                    #     if j:
                    #         temp.append(j.val)
            ans.append(ans_each)
            curr = temp
        return ans

