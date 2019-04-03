class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        lenFlower = len(flowerbed)
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        for idx in range(1, lenFlower + 1):
            if flowerbed[idx] == 0 and flowerbed[idx - 1] == 0 and flowerbed[idx + 1] == 0:
                n -= 1
                flowerbed[idx] = 1
                if n == 0:
                    break
            else:
                continue
        return n == 0
x = Solution()
x.canPlaceFlowers([1,0,0,0,1,0,0], 2)
