class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search solution, double pass
        # first find the pivot with binary search
        # then search the sorted_left or sorted_right part

        # search the pivot point
        l, r = 0, len(nums) - 1
        # pivot = nums[0]
        pivot_idx = 0
        while(l<r):
            mid = l + (r-l)//2
            

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        pivot = l
        print(pivot)
        l, r = 0, len(nums) - 1
        # is target contained on left part? Or right part
        #if target >= nums[pivot] and target <= nums[r]:
        #    l = pivot
        #else:
        #    r = pivot - 1
        if target == nums[pivot]: return pivot

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        print(r)
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] > target: # search left
                r = mid -1
            else:
                l = mid +1
        return -1