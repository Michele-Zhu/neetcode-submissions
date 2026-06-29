class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for char in s1:
            count_s1[char] = 1 + count_s1.get(char, 0)

        need = len(count_s1)
        for i, char in enumerate(s2):
            count2, current = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count_s1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count_s1.get(s2[j], 0) == count2[s2[j]]:
                    current +=1
                if current == need:
                    return True
        return False
