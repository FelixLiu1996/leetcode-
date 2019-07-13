class Solution:
    def letterCombinations(self, digits):
        # 递归法
        # num_to_letter = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
        #                  '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
        #                  '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        # if not digits:
        #     return []
        # ans = []
        # def helper(i, temp):
        #     # i记录到digits哪一位了
        #     if i == len(digits):
        #         ans.append(temp)
        #         return
        #     for letter in num_to_letter[digits[i]]:
        #         helper(i + 1, temp + letter)
        # helper(0, '')
        # return ans

        # 迭代法
        num_to_letter = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                         '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return []
        ans = ['']  # 必须加引号变成空的字符数组
        for digit in digits:
            next_ans = []
            for letter in num_to_letter[digit]:
                for temp in ans:
                    next_ans.append(temp + letter)  # 这样就能保证数目
            ans = next_ans
        return ans