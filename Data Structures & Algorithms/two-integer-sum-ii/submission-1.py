class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers) - 1
        pairMatch = []
        while leftPtr < rightPtr:
            currentSum = numbers[leftPtr] + numbers[rightPtr]
            if currentSum != target:
                if currentSum < target:
                    leftPtr += 1
                elif currentSum > target:
                    rightPtr -= 1
            else:
                pairMatch.append(leftPtr + 1)
                pairMatch.append(rightPtr + 1)
                return pairMatch
