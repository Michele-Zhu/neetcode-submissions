class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            # y will always be bigger or equal than x
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)

            if x == y:
                continue
            else:  # x < y
                heapq.heappush_max(stones, y - x)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0