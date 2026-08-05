class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # key : value

        for i, val in enumerate(nums):
            if val not in hashmap:
                hashmap[target-val] = i
            else:
                return [hashmap[val], i]