# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        totalDiameter = 0

        def dfs(node):
            nonlocal totalDiameter
            if not node:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            totalDiameter = max(totalDiameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
        dfs(root)

        return totalDiameter
