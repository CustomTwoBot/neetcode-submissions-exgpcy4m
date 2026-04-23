class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefixProduct = 1
        suffixProduct = 1

        for i in range(len(nums)):
            prefixArray = nums[0:i]
            suffixArray = nums[i+1 : len(nums)]
            prefixProduct = math.prod(prefixArray)
            suffixProduct = math.prod(suffixArray)
        
            result.append(prefixProduct * suffixProduct)
        return result
            
        
