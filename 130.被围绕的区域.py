class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 需要找到不在边界点上的O以及不与边界点O相连的O
        # 除了上述的点之外，其余的O都将在遍历之后变成X
        # 所以通过对边界上的点进行dfs，找到所有与边界O相连的O
        # 标记成-，然后再遍历数组，将没有标记的O变成X，标记为-的重新变为O

        if not board or not board[0]:
            return
        nrow = len(board)
        ncol = len(board[0])
        # 对第一行与最后一行进行dfs
        for i in range(0, ncol):
            self.dfs(board, 0, i)
            self.dfs(board, nrow - 1, i)
        # 对第一列与最后一列进行dfs
        for j in range(0, nrow):
            self.dfs(board, j, 0)
            self.dfs(board, j, ncol - 1)
        for i in range(0, nrow):
            for j in range(0, ncol):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'
        return

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i > len(board) - 1 \
            or j > len(board[0]) - 1 or board[i][j] != 'O':
            return
        board[i][j] = '-'
        self.dfs(board, i - 1, j)  # 递归调用该点上方的点
        self.dfs(board, i + 1, j)  # 递归调用该点下方的点
        self.dfs(board, i, j - 1)  # 递归调用该点左方的点
        self.dfs(board, i, j + 1)  # 递归调用该点右方的点
        return

