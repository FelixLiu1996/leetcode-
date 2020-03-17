class Solution:
    def divisorGame(self, N):
        # 偶数先手赢
        # 因为总能让后手拿到的是奇数
        # 最后最小的偶数是2 先手-1，后手拿到1 输
        if N % 2 == 0:
            return True
        else:
            return False