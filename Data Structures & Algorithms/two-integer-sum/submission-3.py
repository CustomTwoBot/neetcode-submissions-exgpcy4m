class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                complement = target - nums[i]
                hashmap[complement] = i
            else:
                return [hashmap.get(nums[i]), i]


            
        