class Solution:
    def fib(self, N: int) -> int:
        Fib = [0, 1]
        i = 2
        while i <= N:
            Fib.append(Fib[i] + Fib[i - 1])
        return Fib[N]