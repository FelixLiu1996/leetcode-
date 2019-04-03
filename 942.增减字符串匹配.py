class Solution:
    def diStringMatch(self, S):
        N = len(S)
        num = [i for i in range(0, N + 1)]
        ans = []
        i = 0
        while i < N:
            if S[i] == 'I':
                ans.append(num[0])
                num.pop(0)
            if S[i] == 'D':
                ans.append(num[len(num) - 1])
                num.pop()
            i += 1
        ans.append(num[0])
        return ans
x = Solution()
print(x.diStringMatch('IDID'))

