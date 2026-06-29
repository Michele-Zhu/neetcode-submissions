class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def binary_search(low, high):
            if low > high:
                return
            
            mid = low + (high - low) // 2
            # compute eating time
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p)/mid)
            if total_time <= h:
                self.speed = min(mid, self.speed)
                # keep search left
                binary_search(low, mid-1)
            else:
                binary_search(mid+1, high)
        piles.sort()
        left, right = 1, piles[-1]
        self.speed = piles[-1]
        binary_search(left, right)
        return self.speed