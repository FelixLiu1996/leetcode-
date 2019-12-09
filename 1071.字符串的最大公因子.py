class Solution:
    def gcdOfStrings(self, str1: str, str2: str):
        # 辗转相除法
        # 用长的减去短的
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        str2_new = str2.replace(str1, "")
        if str2_new == "":
            return str1
        elif str2 == str2_new:
            return ""
        else:
            self.gcdOfStrings(str1, str2_new)

