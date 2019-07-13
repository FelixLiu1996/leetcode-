class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力法 实在是太慢了

        # if not s:
        #     return 0
        # self.ans = -1
        # n = len(s)
        # def helper(i):
        #     temp = []
        #     string = s[i:]
        #     for j in string:
        #         if j not in temp:
        #             temp.append(j)
        #         else:
        #             break
        #     if len(temp) > self.ans:
        #         self.ans = len(temp)
        # for i in range(n):
        #     helper(i)
        # return self.ans

        # 滑动窗口
        # 比如abc这个窗口满足题目要求，当再进入a/b/c时，这时候不满足要求，这时候移动这个队列
        # 一直维持这样的队列，找出队列出现最长的长度时候，求出解
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                # 窗口向右移
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


