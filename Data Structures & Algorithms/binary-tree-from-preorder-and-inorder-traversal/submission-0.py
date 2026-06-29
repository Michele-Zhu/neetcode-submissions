# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            # what's the exit condition? 
            # left -> left idx for inorder, right -> right idx for inorder
            if left > right:
                return None
            # slide preorder to get the currrent node/root of subtree
            node_val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            node = TreeNode(node_val)
            # index the inorder to get the position
            mid = inorder_idx[node_val]
            node.left = dfs(left, mid-1)
            node.right = dfs(mid+1, right)
            return node

        # we are supposing that each node is unique
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0
        return dfs(0, len(inorder)-1)