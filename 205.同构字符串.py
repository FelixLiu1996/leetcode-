class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t:
            return True
        dic = {}
        t = list(t)
        s = list(s)
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            elif s[i] not in dic:
                dic[s[i]] = t[i]
                if len(dic.values()) != len(list(set(dic.values()))):
                    return False
        return True
x = Solution()
print(x.isIsomorphic(s = "egg", t = "add"))
