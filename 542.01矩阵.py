class Solution:
    def updateMatrix(self, matrix):
        # BFS
        queue = []
        visited = set()
        #visited = []  使用列表超时
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        while queue:
            i, j = queue.pop(0)
            print((i, j))
            for (x, y)  in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1
                    queue.append((x, y))
                    visited.add((x, y))
        return matrix

matrix = [[0,0,0],[0,1,0],[0,0,0]]
x = Solution()
print(x.updateMatrix(matrix))