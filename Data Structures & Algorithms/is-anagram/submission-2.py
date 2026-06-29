class Solution:
    def __init__(self):
        self.c = 30

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
        
        s_count = self.count_letters(s)
        t_count = self.count_letters(t)
        if len(s_count) != len(t_count) :
            return False
        for key, value in s_count.items() :
            if t_count.get(key) != value :
                return False
            
        return True
            
        