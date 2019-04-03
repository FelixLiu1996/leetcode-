class Solution:
    def repeatedStringMatch(self, A: str, B: str):
        n = len(B) // len(A) + 2
        if list(set(B) - set(A)) != []:
            return -1
        else:
            for i in range(1, n + 1):
                if B in A * i:
                    return i
            return -1

x = Solution()
print(x.repeatedStringMatch(A = "abcd",B = "cdabcdab"))
