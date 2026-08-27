class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            parent[rootB] = rootA

            return True


        for node1, node2 in edges:
            if union(node1, node2) == True:
                count += 1

        
        return n - count            
