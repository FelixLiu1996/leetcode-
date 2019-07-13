class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        # in_degree 存放的是度，循环一遍，后继课程的度均加1
        # adj存放的后继课程的集合
        in_degree = [0] * numCourses
        adj = [set() for i in range(numCourses)]
        for first, second in prerequisites:
            in_degree[first] += 1
            adj[second].add(first)
        # 循环一遍，把所有度为0的节点放到队列中
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            temp = queue.pop(0)
            count += 1
            # 当先修课程可以学习时，后继课程的度减1
            # 若后继课程的度变为0，则说明可以学习了，故加入队列中
            for second in adj[temp]:
                in_degree[second] -= 1
                if in_degree[second] == 0:
                    queue.append(second)
        return count == numCourses
