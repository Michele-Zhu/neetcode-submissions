# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, depth):
        if node is None:
            return depth
        
        left = self.dfs(node.left, depth + 1)
        right = self.dfs(node.right, depth + 1)
        return max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)