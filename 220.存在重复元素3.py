class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int):
        nums_idxs = []
        for i, num in enumerate(nums):
            # 保存[值，索引]
            nums_idxs.append([num, i])
        # 根据值的大小排序

        nums_idxs.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # 若值之差已经大于t 则直接跳出当前循环
                if nums_idxs[j][0] - nums_idxs[i][0] > t:
                    break
                if abs(nums_idxs[i][1] - nums_idxs[j][1]) <= k:
                    return True
        return False

