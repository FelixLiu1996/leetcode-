class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        idx1, idx2 = 0, 0
        last = None
        while idx2 < len(typed) and idx1 < len(name):
            if name[idx1] == typed[idx2]:
                last = name[idx1]
                idx1 += 1
                idx2 += 1
            elif typed[idx2] == last:
                idx2 += 1
            else:
                return False
        while idx2 < len(typed) and typed[idx2] == last:
            idx2 += 1
        return idx1 == len(name) and idx2 == len(typed)
x = Solution()
print(x.isLongPressedName("jveznlsjalhrnvmedogfydxnyvhmcjycgbwrpmgpsueqrpsnyqqadptdqetvqbhhmupzsdzbiqkahgupdwfiwtknzssrzyhlqgqxhjlkqbuhqlponeackgmmndmyeaiswcaiqxiudqgtxlrjwkpzolcynsrgqcbvphnoradctlfjrloykccsicuxcqtgvrlegvesooad",\
"jvveznlssjjalhhrrnnvvmeedooggffyydxnyyvvhmcjjyyccgbwwrrpmmggppssueqrrpsnnyqqqqaaddpptdqetvvqqbhhhhmmuupzzssdzbiiqkkaahhguuppddwwffiwwtkknnzzssssrrzzyhlqqggqxhjlkqbuuhqqlponneaackkggmmmndmyyeaiiswccaiiqxiiudqggttxllrrjjwkkpzoolcynsrrggqcbvvpphhnorraddcctlffjrrllooykccccsiicuuxccqqttggvrrlleegvvesoooad"))