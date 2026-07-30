class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(len(nums)):
            if len(nums) <= 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums[0], nums[1])
            rob1 = dp[i-1]
            rob2 = dp[i-2]
            dp[i] = max(rob1, nums[i] + rob2)

        return dp[len(nums)-1]

        