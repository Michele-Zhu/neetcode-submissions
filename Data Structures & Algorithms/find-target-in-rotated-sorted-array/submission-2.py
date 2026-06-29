class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search solution
        def binary_search(low, high):
            if low > high:
                return -1
            
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            
            # left part is sorted
            if nums[low] <= nums[mid]:
                if target < nums[mid] and target >= nums[low]:
                    # search left
                    print("nums[low] <= mid & search left")
                    return binary_search(low, mid-1)
                else:
                    print("nums[low] <= mid & search right")
                    return binary_search(mid + 1, high)
            else: # right part contains the rotation
                if target > nums[mid] and target <= nums[high]:
                    # search right
                    return binary_search(mid+1, high)
                else: 
                    return binary_search(low, mid-1)
        
        return binary_search(0, len(nums)-1)