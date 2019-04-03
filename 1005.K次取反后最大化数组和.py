class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        while K > 0:
            A.sort()
            A[0] = -A[0]
            K -= 1
        return sum(A)
