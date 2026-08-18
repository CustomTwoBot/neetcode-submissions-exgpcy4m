class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
       rows, cols = len(grid), len(grid[0])
       count = 0

       def bfs(r, c):
            queue = deque()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            grid[r][c] = "0"
            queue.append((r,c))
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0":
                        continue

                    queue.append((nr,nc))
                    grid[nr][nc] = "0"
                
       for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
       return count



                    
