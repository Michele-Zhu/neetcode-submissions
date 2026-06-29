class Solution:

    def count_letters(self, string : str) :
        hash_table = {}
        for char in string :
            if hash_table.get(char) == None :
                hash_table[char] = 1
            else :
                hash_table[char] +=1
        return(hash_table)
        
    def isAnagram(self, s: str, t: str) -> bool :
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t
            
        