class Solution:
    def findErrorNums(self, nums):
        check = [0] * len(nums)
        loss = 0
        redudent = 0
        for i in nums:
            check[i - 1] += 1
        for i in range(len(check)):
            if check[i] == 0:
                loss = i + 1
            if check[i] == 2:
                redudent = i + 1
        return [redudent, loss]


        #若是首位1未出现则错误
        # ans = []
        # nums_hash = list(enumerate(sorted(nums), start=1))
        # print(nums_hash)
        # for i in nums_hash:
        #     if i[0] != i[1]:
        #        ans.append(i[1])
        #        ans.append(i[0])
        # return ans

x = Solution()
print(x.findErrorNums([1,2,2,4]))
