class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxIsland = 0

        def dfs(r, c):
            stack = [[r,c]]
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            count = 1
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue
                    visited.add((nr, nc))
                    count += 1
                    stack.append((nr, nc))
            
            return count
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    visited.add((r,c))
                    maxIsland = max(maxIsland, dfs(r, c))
        
        return maxIsland