from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        # f = [0] * (n + 1)
        # x = 1
        # for i in range(1, n + 1):
        #     if x ** 2 == i:
        #         f[i] = 1
        #         x += 1
        #     min_val = 10000000000
        #     for k in range(1 ,int(sqrt(i)) + 1):
        #         min_val = min(min_val, f[i - k ** 2])
        #     f[i] = 1 + min_val
        # return f[n]

        # ans = n
        # maxn = int(sqrt(n))
        # dp = [i for i in range(n + 1)]
        # for i in range(1 , maxn + 1):
        #     for j in range(i * i, n + 1):
        #         dp[j] = min(dp[j], dp[j - i ** 2] + 1)
        # return dp[n]

        # Approach two 利用队列和BFS，最先搜索到的结果一定是最短的。 队列中存储（位置,步数） ，效率比较低。
        q = [[n, 0]]
        visited = [False for _ in range(n + 1)]
        visited[n] = True
        while q:
            num, step = q.pop(0)   # 出栈，被pop掉的元素将同时返回给两个变量
            i = 1
            tnum = num - i ** 2
            while tnum >= 0:            # 前进一步
                if tnum == 0: return step + 1   # 最先到达0的一定是步数最少的
                if not visited[tnum]:
                    q.append((tnum, step + 1))
                    visited[tnum] = True     # 只添加没有遍历过的节点，减少计算量
                i += 1
                tnum = num - i ** 2


x = Solution()
print(x.numSquares(8829))
