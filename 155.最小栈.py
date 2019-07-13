class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.Min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.Min or x <= self.Min[-1]:
            self.Min.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.Min[-1]:
            self.Min.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        return self.Min[-1] if self.Min else -1

#  这样太慢
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         # if len(self.stack) > 0:
#         #     return min(self.stack)
#         # else:
#         #     return None
#         return min(self.stack)
