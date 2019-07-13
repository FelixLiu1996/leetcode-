class Solution:
    def generateParenthesis(self, n) -> list[str]:
        # 回溯法
        # 只有仍然有效的括号排列才能继续进行添加括号，一直到n个括号组被用完
        # 满足条件的添加入ans
        ans = []
        def check(left_parenthesis, right_parenthesis, temp):
            if left_parenthesis == 0 and right_parenthesis == 0:
                ans.append(temp)
            if left_parenthesis < 0 or right_parenthesis < 0 or left_parenthesis > right_parenthesis:
                # 判断条件为 此括号排列无效
                return
            check(left_parenthesis - 1, right_parenthesis, temp + '(')
            check(left_parenthesis, right_parenthesis - 1, temp + ')')

        check(n, n, '')
        return ans

