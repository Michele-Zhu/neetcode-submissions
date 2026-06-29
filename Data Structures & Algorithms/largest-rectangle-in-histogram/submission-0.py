class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left_most = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_most[i] = stack[-1]
            stack.append(i)

        stack = []
        right_most = [n]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_most[i] = stack[-1]
            stack.append(i)

        max_area = 0
        for i in range(n):
            left_most[i] += 1
            right_most[i] -= 1
            max_area = max(max_area, heights[i] * (right_most[i] - left_most[i] + 1))
        return max_area