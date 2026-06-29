class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate_distance(x1, y1):
            # distance to the origin (0, 0)
            # return math.sqrt(x1**2 + y1**2)
            # we only need the relative distance
            return x1 ** 2 + y1 ** 2
        
        heap = []
        heapq.heapify_max(heap)

        # O(n) time, n len of points, 
        # O(k) space
        for point in points:
            # print(point, str(type(point)))
            
            d = calculate_distance(point[0], point[1])
            heapq.heappush_max(heap, [d, point[0], point[1]]) # O(log k)
            if len(heap) > k:
                heapq.heappop_max(heap)  # O(log k)
        
        return [[item[1], item[2]] for item in heap]