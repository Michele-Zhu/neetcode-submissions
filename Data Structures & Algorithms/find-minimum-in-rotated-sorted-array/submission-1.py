class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search(low, high):
            if low > high:
                # print(f"low>high, index {low, high}")
                return
            if nums[low] < nums[high]:
                # print(f"nums[low] < nums[high], index {low, high}")
                self.result = min(self.result, nums[low])
                return

            mid = low + (high - low) // 2
            # print(f"visiting mid {mid} with value {nums[mid]}")
            self.result = min(self.result, nums[mid])
            if nums[mid] >= nums[low]: # got right
                return binary_search(mid+1, high)
            else:
                return binary_search(low, mid-1)
        self.result = nums[0]
        binary_search(0, len(nums)-1)
        return self.result