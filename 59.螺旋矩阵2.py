class Solution:
    def generateMatrix(self, n: int):
        #matrix = [[0] * n] * n
        matrix = [[0 for i in range(n)] for j in range(n)]
        di, dj = 0, 1
        i, j = 0, 0
        for k in range(n * n):
            matrix[i][j] = k + 1
            #flag_matrix[i][j] = False
            if matrix[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return matrix
x = Solution()
print(x.generateMatrix(3))

