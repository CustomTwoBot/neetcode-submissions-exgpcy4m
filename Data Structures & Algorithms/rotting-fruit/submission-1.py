class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue:
            anyRotted = False
            size = len(queue)
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for _ in range(size):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        anyRotted = True
            if anyRotted:
                minutes += 1
        
        for cr in range(rows):
            for cc in range(cols):
                if grid[cr][cc] == 1:
                    return -1
        return minutes

                
        
