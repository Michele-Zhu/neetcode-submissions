class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # At each heights we compute the widest area that 
        # bar can occupy, so we need to find left/right boundaries
        # the boundaries is the index where we find the first 
        # bar with lower height
        # this can be done iteratively at each height using left and
        # right pointers -> solution is O(n^2)
        # using a stack as supporting data structure
        # we iterate the array, we use a monotonic stack which track
        # the index where that height can start

        # Area = h * width
        # width = right_boundary_idx - left_boundary idx - 1

        n = len(heights)
        # Monotonic stack that tracks bars and its start at, increasing h order
        stack = []
        left_most = [-1] * n
        for i in range(n):
            # The stack is popped until is smaller than current h
            # we found a left boundary
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_most[i] = stack[-1]
            stack.append(i)

        stack = []
        right_most = [n] * n
        for i in reversed(range(0, n)):
            #print(i)
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_most[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(n):

            max_area = max(max_area, heights[i]* (right_most[i] - left_most[i] - 1))
        return max_area
