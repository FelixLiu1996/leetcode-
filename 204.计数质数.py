class Solution:
    def countPrimes(self, n: int) -> int:
        """prime存放素数， pnum表示素数的个数，p判断是否是素数"""
        prime = []
        pnum = 0
        p = [False] * (n + 1)
        for i in range(2, n):
            if p[i] == False:
                pnum += 1
                p[i:n:i] = [True] * len(p[i:n:i])
        return pnum
        # for i in range(2, n):
        #     if p[i] == False:
        #         prime.append(i)
        #         pnum += 1
        #         j = i
        #         while j < n:
        #             p[j] = True
        #             j += i
        # return pnum
x = Solution()
print(x.countPrimes(10))
