class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}

        for value in nums:
            if hash_table.get(value) is None:
                hash_table[value] = True
            else:
                return True
                
        return False
