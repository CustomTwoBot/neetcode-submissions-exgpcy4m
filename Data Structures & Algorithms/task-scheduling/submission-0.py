class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                x = heapq.heappop(maxHeap) + 1
                if x < 0:
                    queue.append((x, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time 