class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        maxKValues = k

        while maxKValues > 0:
            max_key = max(hashmap, key = hashmap.get)
            res.append(max_key)
            del hashmap[max_key]
            maxKValues -= 1
        
        return res
