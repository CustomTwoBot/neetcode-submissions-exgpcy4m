class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        cycles = 0
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()

        while queue or maxHeap:
            cycles += 1
            if maxHeap:
                x = heapq.heappop(maxHeap) + 1

                if x < 0:
                    queue.append((x, cycles + n))
            
            if queue and queue[0][1] == cycles:
                heapq.heappush(maxHeap, queue.popleft()[0])
            
        return cycles

