class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val : index
        for i, val in enumerate(nums):
            difference = target - val
            if difference not in hashmap:
                hashmap[val] = i
            else:
               return [hashmap[difference], i]
            
        