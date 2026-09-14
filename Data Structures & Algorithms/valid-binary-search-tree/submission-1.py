# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            size = len(queue)
            for _ in range(size):
                node, low, high = queue.popleft()

                if not (low < node.val < high):
                    return False
                if node:
                    if node.left: 
                        queue.append((node.left, low, node.val))
                    if node.right:
                        queue.append((node.right, node.val, high))
        
        return True
