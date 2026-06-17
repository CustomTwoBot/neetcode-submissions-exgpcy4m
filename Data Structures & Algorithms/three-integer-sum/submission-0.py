class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutionList = []

        for i in range(len(nums) - 1):
            leftPtr = i + 1
            rightPtr = len(nums) - 1

            while leftPtr < rightPtr:
                sum = nums[leftPtr] + nums[rightPtr] + nums[i]

                if sum > 0:
                    rightPtr -= 1
                elif sum < 0:
                    leftPtr += 1
                else:
                    sol = [nums[leftPtr], nums[i], nums[rightPtr]]
                    if sol not in solutionList:
                        solutionList.append(sol)
                    leftPtr += 1
                    rightPtr -= 1
        return solutionList
            
                

