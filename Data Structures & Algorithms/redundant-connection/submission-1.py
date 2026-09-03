class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        answerArray = []

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
        
        for i,j in edges:
            if union(i,j) == False:
                answerArray.append([i,j])

        return answerArray[-1] 


            