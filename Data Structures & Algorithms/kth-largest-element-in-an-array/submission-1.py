class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Since you have to return the k-th largest item 
        # you can use a min-heap that contains k elements
        # when min-heap > k you pop the min
        # heap[0] effectively contains the kth largest element
        heap = nums
        heapq.heapify(nums)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]