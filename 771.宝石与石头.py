class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = list(J)
        S = list(S)
        ans = 0
        for j in J:
            ans += S.count(j)
        return ans

x = Solution()
print(x.numJewelsInStones("aA", "aAAbbbb"))