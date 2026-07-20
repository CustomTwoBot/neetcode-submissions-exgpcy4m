class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high

        while low <= high:
            k = (low + high) // 2
            time = 0

            for i in piles:
                time += math.ceil(i / k)
            
            if time <= h:
                high = k-1
                result = k
            else:
                low = k+1
            
        return result

