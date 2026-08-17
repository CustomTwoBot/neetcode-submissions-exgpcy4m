class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dpMin = [0] * len(nums)
        dp[0] = nums[0]
        dpMin[0] = nums[0]

        for i in range(1, len(nums)):
            calc1 = nums[i] * dp[i-1]
            calc2 = nums[i] * dpMin[i-1]

            dpMin[i] = min(nums[i], calc1, calc2)
            dp[i] = max(nums[i], calc1, calc2)
        
        return max(dp)