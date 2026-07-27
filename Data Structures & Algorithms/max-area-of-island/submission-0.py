class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = [0]

        def bfs(r,c) -> int:
            queue = collections.deque()
            area = 0
            area += 1
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()

                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1:
                        area += 1
                        queue.append((r,c))
                        visited.add((r,c))

            return area

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    visited.add((r,c))
                    maxArea.append(bfs(r,c))
        return max(maxArea)
                
