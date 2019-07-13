class Solution:
    def combination(self, candidates, target):
        # 回溯法
        self.ans = []
        candidates.sort()
        def helper(i, temp_sum, temp):
            if temp_sum > target or i == len(candidates):
                return
            if temp_sum == target:
                self.ans.append(temp)
            if temp_sum < target:
                # 这里有两个分支，一个是加上现在所处的元素
                # 另外是不加上现在所处的元素，判断加上下一个元素
                helper(i, temp_sum + candidates[i], temp + [candidates[i]])
                helper(i + 1, temp_sum, temp)

        helper(0, 0, [])
        return self.ans

x = Solution()
print(x.combination([2,3,6,7], 7))