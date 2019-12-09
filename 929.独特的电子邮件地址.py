class Solution:
    def numUniqueEmails(self, emails) -> int:
        # ans = set()
        # for i in range(len(emails)):
        #     temp = emails[i].split('@')
        #     left = list(temp[0])
        #     right = list(temp[1])
        #     left_after = []
        #     for j in range(len(left)):
        #         if left[j] == '.':
        #             continue
        #         elif left[j] == '+':
        #             break
        #         else:
        #             left_after.append(left[j])
        #     ans_each = left_after + ["@"] + right
        #     ans.add(''.join(ans_each))
        # return len(ans)


        ans = set()
        for i in range(len(emails)):
            temp = emails[i].split('@')
            left = temp[0]
            right = temp[1]
            left = left.split('+')[0]
            left = left.replace('.', '')
            ans_each = left + '@' + right
            ans.add(ans_each)
        return len(ans)




a = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(a[0].split('@'))