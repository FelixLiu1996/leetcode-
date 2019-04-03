from math import sqrt
class Solution:
    def kClosest(self, points, K):
        # ans = []
        # eucildDistance = {}
        # for point in points:
        #     eucildDistance[point] = (sqrt(point[0] ** 2 + point[1] ** 2))
        # i = 0
        # while i < k:
        #     ans.append(min(eucildDistance))
        #return sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        def F(a):
            return a[0] ** 2 + a[1] ** 2
        return sorted(points, key=F)[:K]

x = Solution()
print(x.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2))






