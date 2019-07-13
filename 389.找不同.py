class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 计数法
        # a = list(set(list(t)))
        # s = list(s)
        # t = list(t)
        # for i in a:
        #     if s.count(i) != t.count(i):
        #         return i


        #异或法：数字与自身异或为0
        ans = 0
        for i in s + t:
            ans ^= ord(i)
        return chr(ans)
