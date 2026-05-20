class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        consecutiveCounter = 0
        currentNum = 0
        counterList = [0]
        for i in hashset:
            if i-1 not in hashset:
                currentNum = i
                consecutiveCounter += 1

                while currentNum + 1 in hashset:
                    currentNum += 1
                    consecutiveCounter += 1
            counterList.append(consecutiveCounter)
            consecutiveCounter = 0
        return max(counterList)

        
