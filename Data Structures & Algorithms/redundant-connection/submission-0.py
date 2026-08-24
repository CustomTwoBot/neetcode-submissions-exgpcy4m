class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        selectedEdge = []

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
        
        for node1, node2 in edges:
            if union(node1, node2) == False:
                selectedEdge.append([node1, node2])
        
        return selectedEdge[-1]
            