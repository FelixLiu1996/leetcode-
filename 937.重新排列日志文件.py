class Solution:
    def reorderLogFiles(self, logs):
        left = []
        right = []
        for i in range(len(logs)):
            temp = logs[i].split(' ')
            if temp[1].isnumeric():
                right.append(' '.join(temp))
            else:
                left.append(' '.join(temp))
        def compare(x):
            """
            如果不相同，忽略标识符比较
            如果相同，则比较标识符
            """
            x = x.split(' ')
            return (x[1: ], x[0])
        left.sort(key=lambda x: compare(x))
        return left + right

