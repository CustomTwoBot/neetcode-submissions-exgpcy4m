class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            parent[rootB] = rootA
        
            return True
        
        count = n

        for i, j in edges:
            if union(i, j):
                count -= 1
        
        return count