class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _set = set()

        for value in nums:
            if value in _set:
                return True
            else:
                _set.add(value)
        return False