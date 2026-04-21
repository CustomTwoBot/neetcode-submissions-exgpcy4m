class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # Counts amount of times a number shows up
        values = [[] for i in range(len(nums) + 1)] # Stores the numbers themselves
        finalResult = []

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        for n, c in hashmap.items():
            values[c].append(n)
        for i in range(len(values) - 1, 0, -1):
            for n in values[i]:
                finalResult.append(n)
                if len(finalResult) == k:
                    return finalResult



        
            
        