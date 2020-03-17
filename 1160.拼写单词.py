class Solution:
    def countCharacters(self, words, chars):
        if not chars or not words:
            return 0
        char_dic = {}
        for char in chars:
            if char not in char_dic:
                char_dic[char] = 1
            else:
                char_dic[char] += 1
        ans = 0
        for word in words:
            flag = True
            for c in word:
                if c not in char_dic or word.count(c) > char_dic[c]:
                    flag = False
                    break
            if flag:
                ans += len(word)
        return ans

x = Solution()
print(x.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
