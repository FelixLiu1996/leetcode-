class Solution:
    def findOrder(self, numCourses, prerequisites):
        # in_degree存放度
        # adj存放后继课程的集合
        in_degree = [0] * numCourses
        adj = [set() for i in range(numCourses)]
        for second, first in prerequisites:
            in_degree[second] += 1
            adj[first].add(second)
        # queue存放度为0的课程
        # res存放课程的顺序
        queue = []
        res = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            temp = queue.pop(0)
            res.append(temp)
            # 如果先修课程已经学习，那么该课程的后继课程也可进行学习
            for successor in adj[temp]:
                in_degree[successor] -= 1
                if in_degree[successor] == 0:
                    queue.append(successor)
        if len(res) == numCourses:
            return res
        else:
            return []


