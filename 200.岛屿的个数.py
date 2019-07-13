class Solution:
    def numIslands(self, grid) -> int:
        # 本题使用BFS
        if not grid or not grid[0]:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        queue = []
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 使用坐标数组需要添加的东西
        for i in range(nrow):
            for j in range(ncol):
                # 因为网格旁边被水包围，所以只要有1出现，则至少是一个岛屿
                # 只是需要判断与他相连的岛屿，从而确定数目，与之相连的1则算作是同一个岛屿

                if grid[i][j] == '1':
                    queue.append((i, j))
                    grid[i][j] = '-'
                    count += 1
                    while queue:
                        row_station, col_station = queue.pop(0)

                        # 冗余的做法
                        # if 0 <= row_station + 1 < nrow and 0 <= col_station < ncol and grid[row_station + 1][col_station] == '1':
                        #     queue.append((row_station + 1, col_station))
                        #     grid[row_station + 1][col_station] = '-'
                        # if 0 <= row_station - 1 < nrow and 0 <= col_station < ncol and  grid[row_station - 1][col_station] == '1':
                        #     queue.append((row_station - 1, col_station))
                        #     grid[row_station - 1][col_station] = '-'
                        # if 0 <= row_station < nrow and 0 <= col_station + 1 < ncol and grid[row_station][col_station + 1] == '1':
                        #     queue.append((row_station, col_station + 1))
                        #     grid[row_station][col_station + 1] = '-'
                        # if 0 <= row_station < nrow and 0 <= col_station - 1 < ncol and grid[row_station][col_station - 1] == '1':
                        #     queue.append((row_station, col_station - 1))
                        #     grid[row_station][col_station - 1] = '-'

                        # 使用坐标数组

                        for (direction_x, direction_y) in directions:
                            if 0 <= row_station + direction_x < nrow and 0 <= col_station + direction_y < ncol \
                                and grid[row_station + direction_x][col_station + direction_y] == '1':
                                queue.append((row_station + direction_x, col_station + direction_y))
                                grid[row_station + direction_x][col_station + direction_y] = '-'

        return count

