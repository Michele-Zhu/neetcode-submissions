# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            # max_val is the maximum value in the path
            if not node:
                return None
            
            # This is a good node
            if node.val >= max_val:
                self.good_count += 1
                max_val = node.val
            
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        self.good_count = 0
        dfs(root, root.val)
        return self.good_count