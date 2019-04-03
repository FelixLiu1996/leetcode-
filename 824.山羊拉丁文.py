class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ans = ''
        # for word in S:
        #     temp = word
        #     if word[0] in vowels:
        #         temp += 'ma'
        #     elif word[0] not in vowels:
        #         temp1 = word[0]
        #         temp = temp[1:]
        #         temp += temp1 + 'ma'
        #     temp = temp + 'a' * (S.index(word) + 1)
        #     ans += temp
        #     if S.index(word) != len(S) - 1:
        #         ans += ' '
        # return ''.join(ans)

        # for i in range(len(S)):
        #     temp = S[i]
        #     if S[i][0] in vowels:
        #         temp += 'ma'
        #     elif S[i][0] not in vowels:
        #         temp1 = S[i][0]
        #         temp = temp[1:]
        #         temp += temp1 + 'ma'
        #     temp = temp + 'a' * (i + 1)
        #     ans += temp
        #     if i != len(S) - 1:
        #         ans += ' '
        # return ''.join(ans)


        for i in range(len(S)):
            temp = S[i]
            if S[i][0] in vowels:
                temp += 'ma'
            elif S[i][0] not in vowels:
                temp1 = S[i][0]
                temp = temp[1:]
                temp += temp1 + 'ma'
            temp = temp + 'a' * (i + 1)
            ans += temp
            if i <len(S) - 1:
                ans += ' '
            return ''.join(ans)
x = Solution()
print(x.toGoatLatin("I speak Goat Latin"))
