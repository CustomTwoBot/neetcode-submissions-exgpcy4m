class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if nums[i] not in hashmap:
                hashmap[complement] = i
            else:
                return [hashmap.get(nums[i]), i]
        