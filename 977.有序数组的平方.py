class Solution:
    def sortedSquares(self, A):
        # for i in range(len(A)):
        #     A[i] = A[i] ** 2
        # A.sort()
        # return A
        return sorted([i**2 for i in A])
