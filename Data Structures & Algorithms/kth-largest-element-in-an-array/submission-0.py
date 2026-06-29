class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solve using sorting
        # then solve using heaps :D
        nums.sort()
        return nums[-k]