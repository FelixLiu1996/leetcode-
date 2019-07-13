class Solution:
    def findRestaurant(self, list1, list2):
        # favorite_both = {}
        # if len(list1) < len(list2):
        #     list1, list2 = list2, list1
        # for i in range(len(list1)):
        #     if list1[i] in list2:
        #         favorite_both[list1[i]] = i + list2.index(list1[i])
        #favorite = sorted(favorite_both.items(), key=lambda x: x[1])
        # ans = []
        # Min = favorite[0][1]
        # for i in favorite:
        #     if i[1] == Min:
        #         ans.append(i[0])
        # return ans
        favorite_1 = {v: i for i, v in enumerate(list1)}
        favorite_2 = {v: i for i, v in enumerate(list2)}
        favorite_both = {}
        for i in favorite_1:
            if i in favorite_2:
                favorite_both[i] = favorite_1[i] + favorite_2[i]
        favorite = sorted(favorite_both.items(), key=lambda x: x[1])
        ans = []
        Min = favorite[0][1]
        for i in favorite:
            if i[1] == Min:
                ans.append(i[0])
        return ans



x = Solution()
print(x.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                       ["KFC", "Shogun", "Burger King"]))