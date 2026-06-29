# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, left, right):
            if not node:
                return True
            # check if the node is in valid range
            if not(left < node.val < right):
                return False
            # check validity of subtrees
            left = is_valid(node.left, left, node.val)
            right = is_valid(node.right, node.val, right)
            return (left and right) 
        return is_valid(root, float("-inf"), float("inf"))
