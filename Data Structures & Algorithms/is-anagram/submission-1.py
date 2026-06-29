class Solution:
    def count_char(self, string):
        hash_table = {}
        for char in string:
            if hash_table.get(char) is None:
                hash_table[char] = 0
            else:
                hash_table[char] += 1
        return hash_table

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = self.count_char(s)
        count_t = self.count_char(t)

        for key, value in count_s.items():
            if count_t.get(key) is None or count_t[key] != value:
                return False
        
        return True