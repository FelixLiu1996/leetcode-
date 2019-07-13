class Solution:
    def subdomainVisits(self, cpdomains):
        # dic = {}
        # ans = []
        # for cpdomain in cpdomains:
        #     time, domain = cpdomain.split(' ')
        #     time = int(time)
        #     if domain in dic:
        #         dic[domain] += time
        #     else:
        #         dic[domain] = time
        #     while domain.find('.') > 0:
        #         domain = domain[domain.find('.') + 1: ]
        #         if domain in dic:
        #             dic[domain] += time
        #         else:
        #             dic[domain] = time
        # for k,v in dic.items():
        #     ans.append(str(v) + ' ' + k)
        # return ans
        dic = {}
        ans = []
        for cpdomain in cpdomains:
            time, domain = cpdomains.split(' ')
            domain = domain.split('.')
            time = int(time)
            count = len(domain)
            for i in range(count):
                temp = '.'.join(domain[i: count])
                if temp in dic:
                    dic[temp] += time
                else:
                    dic[temp] = time
        for k, v in dic.items():
            ans.append(str(v) + ' ' + k)
        return ans