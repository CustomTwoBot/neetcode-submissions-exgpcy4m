class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[math.sqrt(pow(x, 2) + pow(y, 2)), [x, y]] for (x, y) in points]
        count = k
        res = []

        heapq.heapify(points)

        while count:
            x = heapq.heappop(points)
            res.append(x[1])
            count -= 1
        
        return res