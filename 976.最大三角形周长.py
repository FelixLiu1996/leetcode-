class Solution:
    def largestPerimeter(self, A) -> int:
        A.sort()
        while len(A) >= 3:
            if A[-2] + A[-3] > A[-1] and A[-2] - A[-3] < A[-1]:
                #return sum(A[len(A) - 3: len(A)])
                return A[-1] + A[-2] + A[-3]

            else:
                A.pop(len(A) - 1)
        return 0
x = Solution()
print(x.largestPerimeter([3,6,2,3]))