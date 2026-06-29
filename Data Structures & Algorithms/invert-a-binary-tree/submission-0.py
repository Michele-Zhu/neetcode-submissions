# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_invert(self, node):
        if not node:
            return None
        temp = node.left
        node.left = self.dfs_invert(node.right)
        node.right = self.dfs_invert(temp)
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs_invert(root)