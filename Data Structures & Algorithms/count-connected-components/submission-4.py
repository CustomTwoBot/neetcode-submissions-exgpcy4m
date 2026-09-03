class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return True
            
            parent[rootB] = rootA
            
            return False

        for i,j in edges:
            if union(i, j) == False:
                count -= 1
            
        return count             
