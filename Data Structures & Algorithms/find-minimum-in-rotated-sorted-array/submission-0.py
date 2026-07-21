class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = 1000
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                minVal = min(nums[left], minVal)
                right -= 1
            else:
                minVal = min(nums[right], minVal)
                left += 1

        return minVal