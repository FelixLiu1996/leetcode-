class Solution:
    def myAtoi(self, str: str) -> int:
        ans = ""
        str = str.strip(" ")
        str_list = str.split(" ")
        print(str_list)
        if str_list[0][0] == '-':
            ans += '-'
            str_list[0] = str_list[0][1:]
            print(str_list)
        for str_each in str_list:
            for each in str_each:
                if each in "01233456789.":
                    ans += each

        return eval(ans)
a = '3.14159'
b = '3'
s = Solution()
print(s.myAtoi(a))
