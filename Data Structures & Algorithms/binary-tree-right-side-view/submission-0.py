# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            size = len(queue)
            levelArray = []

            for _ in range(size):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    levelArray.append(node.val)
            if levelArray:
                res.append(levelArray[-1])
        
        return res
            
