class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # str = list(str.split(' '))
        # pattern = list(pattern)
        # if len(pattern) != len(str):
        #     return False
        # dic = {}
        # temp = []
        # for i in range(len(pattern)):
        #     if pattern[i] in dic:
        #         temp.append(dic[pattern[i]])
        #     else:
        #         dic[pattern[i]] = str[i]
        #         if len(dic.values()) != len(list(set(dic.values()))):
        #             return False
        #         temp.append(str[i])
        # return temp == str
        str = list(str.split(' '))
        pattern = list(pattern)
        dic = {}
        if len(pattern) != len(str):
            return False
        if len(list(set(str))) != len(list(set(pattern))):
            return False
        for i, v in enumerate(pattern):
            if v not in dic:
                dic[v] = str[i]
            else:
                if dic[v] != str[i]:
                    return False
        return True
x = Solution()
print(x.wordPattern("abba","dog dog dog dog"))