class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # dic = {}
        # for i in range(len(s)):
        #     if s[i] in dic:
        #         dic[s[i]] += 1
        #     else:
        #         dic[s[i]] = 1
        # for i in range(len(t)):
        #     if t[i] in dic and dic[t[i]] > 0:
        #         dic[t[i]] -= 1
        #     else:
        #         return False
        # return True

        if len(s) != len(t):
            return False
        a = list(set(s))
        for i in a:
            if s.count(i) != t.count(i):
                return False
        return True