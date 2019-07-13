# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return None
#         def dfs(node, hashd):
#             if node in hashd:
#                 return hashd[node]
#             node_copy = Node(node.val, [])
#             hashd[node] = node_copy
#             for n in node.neighbors:
#                 n_copy = dfs(n, hashd)
#                 if n_copy:
#                     node_copy.neighbors.append(n_copy)
#             return node_copy
#         node_copy = dfs(node, dict())
#         return node_copy


# BFS 做法2
# 利用队列实现

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        queue = [node]
        node_copy = {}
        node_copy[node] = Node(node.val, [])

        while queue:
            vertex = queue.pop(0)
            for v in vertex.neighbors:
                if v not in node_copy:
                    node_copy[v] = Node(v.val, [])
                    queue.append(v)
                node_copy[vertex].neighbors.append(node_copy[v])
        return node_copy[node]




