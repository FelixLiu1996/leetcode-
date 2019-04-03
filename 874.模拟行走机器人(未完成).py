class Solution:
    def robotSim(self, commands, obstacles) -> int:
        obstacles = list(set(map(tuple, obstacles)))
        ans = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        for command in commands:
            #向右转
            if command == -1:
                di = (di + 1) % 4
            #向左转
            elif command == -2:
                di = (di - 1) % 4
            else:
                for k in range(command):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x ** x + y ** y)
        return ans





