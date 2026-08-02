class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        totalMins = 0
        freshFruits = 0
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    freshFruits += 1
        
        while queue and freshFruits > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        freshFruits -= 1
                        queue.append((r,c))
            totalMins += 1
                
        

        return totalMins if freshFruits == 0 else -1
                
        
