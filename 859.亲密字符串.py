class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            st = set(A)
            for s in st:
                if A.count(s) >= 2:
                    return True
                else:
                    return False
        else:
            left = 0
            right = len(A) - 1
            """找到两个不同的字母"""
            while left < right:
                if A[left] != B[left]:
                    break
                left += 1

            while left < right:
                if A[right] != B[right]:
                    break
                right -= 1
            return A[:left] + A[right] + A[left + 1: right] + A[left] == B
