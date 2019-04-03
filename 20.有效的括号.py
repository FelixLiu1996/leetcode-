class Solution:
    def isValid(self, s: str) -> bool:
        List = list(s)
        if List.count('(') != List.count(')') or List.count('[') != List.count(']') \
            or List.count('{') != List.count('}'):
            return False
        else:
            idx = 0
            temp = []
            while idx < len(List):
                if List[idx] in ['(', '[', '{']:
                    temp.append(List[idx])
                    idx += 1

                elif List[idx] in [')', ']', '}']:
                    temp1= List[idx]
                    temp2 = temp.pop()
                    if (temp2, temp1) not in (('(', ')'), ('[', ']'), ('{', '}')):
                        return False
                    else:
                        idx += 1
            return True

x = Solution()
print(x.isValid("()[]"))
