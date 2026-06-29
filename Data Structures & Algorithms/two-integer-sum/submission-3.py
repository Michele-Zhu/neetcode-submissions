class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if hash_table.get(difference) is not None:
                return [hash_table[difference], i]
            else:
                hash_table[nums[i]] = i
        return []