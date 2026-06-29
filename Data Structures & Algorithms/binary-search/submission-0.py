class Solution:
    def _binary_search(self, low: int, high: int, nums: List[int], target: int) -> int:
        if high < low:  # base case
            return -1
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self._binary_search(low, mid-1, nums, target)
        else:
            return self._binary_search(mid+1, high, nums, target)


    def search(self, nums: List[int], target: int) -> int:
        return self._binary_search(0, len(nums)-1, nums, target)