class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        count = k

        while count > 0:
            val = heapq.heappop(nums)
            count -= 1
            
            if count == 0:
                return val * -1
        return 0
