class Solution:
    def reverSeOnlyLetterS(Self, S: Str):
        S = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            # 如果不是字母
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
        return ''.join(S)
