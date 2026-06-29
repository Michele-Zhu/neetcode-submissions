# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs_lowest_common_ancestor(node, p, q):
            if not node or not p or not q:
                return None

            # LCA is on the left subtree
            if max(p.val, q.val) < node.val:
                return dfs_lowest_common_ancestor(node.left, p, q)
            if min(p.val, q.val) > node.val:
                return dfs_lowest_common_ancestor(node.right, p, q)
            else:
                return node
        return dfs_lowest_common_ancestor(root, p, q)