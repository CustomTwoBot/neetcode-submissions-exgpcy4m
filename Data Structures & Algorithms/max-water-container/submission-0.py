class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areaStorage = []
        i = 0
        j = len(heights) - 1

        while i < j:
            areaCalculation = (j - i) * min(heights[i], heights[j])
            areaStorage.append(areaCalculation)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max(areaStorage)
            