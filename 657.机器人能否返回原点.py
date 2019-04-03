class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # xy = [0, 0]
        # for i in moves:
        #     if i == 'R':
        #         xy[0] += 1
        #     elif i == 'L':
        #         xy[0] -= 1
        #     elif i == 'U':
        #         xy[1] += 1
        #     else:
        #         xy[1] -= 1
        # return xy == [0,0]
        """复杂度更小的方法"""
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')