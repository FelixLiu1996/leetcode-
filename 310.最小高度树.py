# class Solution:
#     def dinMinHeightTrees(self, n, edges):
#         if len(edges) <= 1:
#             return edges
#         degree = [0] * n
#         adj = [set() for _ in range(n)]
#         for i, j in edges:
#             degree[i] += 1
#             degree[j] += 1
#             adj[i].add(j)
#             adj[j].add(i)
#         res = []
#         index = -1
#         max_degree = -1
#         for i in range(n):
#             if degree[i] > max_degree:
#                 index = i
#                 max_degree = degree[i]
#         res.append(index)
#         for j in adj[index]:
#             if degree[j] > 1:
#                 res.append(j)
#         return res
#
dic = {'a': [1]}
a = dic.get('d', 'b') + 'ss'
b = dic.get('a', 3) + [3]
print(a)
print(b)