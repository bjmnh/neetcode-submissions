class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxa = 0
        for idx, num in enumerate(heights):
            start = idx
            if stack and num > stack[-1][1]:
                stack.append([idx,heights[idx]])
            else:
                while stack and num <= stack[-1][1]:
                    index, height = stack.pop()
                    maxa = max(height*(idx - index), maxa)
                    start = index
                stack.append([start,heights[idx]])
        while stack:
            index, height = stack.pop()
            maxa = max(height*(len(heights) - index), maxa)
        return maxa

