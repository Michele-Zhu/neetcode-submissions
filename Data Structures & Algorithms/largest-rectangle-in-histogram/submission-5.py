class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack One pass
        
        max_area = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            # top is greater than h, means that 
            # we did not find the left boundary
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h*(len(heights) - i))
        return max_area