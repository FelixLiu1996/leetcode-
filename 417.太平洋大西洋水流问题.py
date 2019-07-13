class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return None
        nrow = len(matrix)
        ncol = len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # queue = []
        # visited = set()
        p_visited = [[0 for i in range(ncol)] for j in range(nrow)]
        a_visited = [[0 for i in range(ncol)] for j in range(nrow)]
        ans = []
        def dfs(matrix, i, j, nrow, ncol, visited):
            visited[i][j] = 1
            # print(visited)

            for (direc_x, direc_y) in directions:
                x, y = i + direc_x, j + direc_y
                # if 0 <= x < nrow and 0 <= y < ncol and not visited[x][y] \
                #     and matrix[x][y] >= matrix[i][j]:
                #     dfs(matrix, x, y, nrow, ncol, visited)
                # else:
                #     continue
                if x < 0 or x >= nrow or y < 0 or y >= ncol or visited[x][y] \
                        or matrix[i][j] > matrix[x][y]:
                    continue
                dfs(matrix, x, y, nrow, ncol, visited)


        for i in range(nrow):
            dfs(matrix, i, 0, nrow, ncol, p_visited)
            dfs(matrix, i, ncol - 1, nrow, ncol, a_visited)
        for j in range(ncol):
            dfs(matrix, 0, j, nrow, ncol, p_visited)
            dfs(matrix, nrow - 1, j, nrow, ncol, a_visited)

        for i in range(nrow):
            for j in range(ncol):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i, j])
        return ans




matrix = [[1,1,1]]

x = Solution()
print(x.pacificAtlantic(matrix))
