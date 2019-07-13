class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # 说明旋转点在mid的右边
                left = mid + 1
            else:
                # 说明旋转点在mid的左边
                right = mid
        rotation = left
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            realmid = (mid + rotation) % n
            if nums[realmid] ==target:
                return realmid
            elif nums[realmid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1