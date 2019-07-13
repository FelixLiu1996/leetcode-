class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 双指针法
        # 首先将left，right分别指向height的左右两端
        # 要想面积最大，只有可能是将left或者right中小的那个往中间移动，才有可能抵消因为底变窄而造成的面积缩小
        # 且有可能使得面积增大
        # if not height:
        #     return 0
        # left = 0
        # right = len(height) - 1
        # max_area = 0
        # while left < right:
        #     max_area = max(max_area, min(height[left], height[right]) * (right - left))
        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return max_area

        if not height:
            return 0
        max_area = 0
        n = len(height)
        for i in range(n - 1):
            for j in range(i + 1, n):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area



