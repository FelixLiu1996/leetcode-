class Solution:
    def compress(self, chars):
        # dic = {}
        # for i in chars:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        charslist = list(set(chars))
        charslist.sort(key=chars.index)
        temp = []
        for i in charslist:
            if chars.count(i) == 1:
                temp.append(i)
            elif 1 < chars.count(i) < 10:
                temp.append(i)
                temp.append(str(chars.count(i)))
            elif chars.count(i) >= 10:
                    temp.append(i)
                    quantity = chars.count(i)
                    while quantity > 0:
                        temp.insert(temp.index(i) + 1, str(quantity % 10))
                        quantity //= 10
        chars = temp
        return chars
x = Solution()
print(x.compress(["a"]))



