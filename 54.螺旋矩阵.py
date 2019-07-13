class Solution:
    def spiralOrder(self, matrix):
        r, i, j, di, dj = [], 0, 0, 0, 1
        if matrix != []:
            for k in range(len(matrix) * len(matrix[0])):
                r.append(matrix[i][j])
                matrix[i][j] = False
                if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == False:
                    di, dj = dj, -di
                i += di
                j += dj
        return r
x = Solution()
print(x.spiralOrder([[ 1, 2, 3, 4],[ 5, 6, 7, 8]]))