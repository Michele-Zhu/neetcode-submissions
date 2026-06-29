# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_balanced(self, node):
        # the tree is not a node, return 0
        if not node:
            return 0

        left = self.dfs_balanced(node.left)
        right = self.dfs_balanced(node.right)

        # subtree is unbalanced
        if left == -1 or right == -1:
            return -1

        # unbalanced condition
        if abs(right - left) > 1:
            return -1
        else:
            return max(left, right) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs_balanced(root) != -1
        