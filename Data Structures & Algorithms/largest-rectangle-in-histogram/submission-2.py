class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: [height : index]
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                height, index = stack.pop()
                maxArea = max(maxArea, height * (i - index))

                start = index
            stack.append([h, start])
        
        for height, index in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea
