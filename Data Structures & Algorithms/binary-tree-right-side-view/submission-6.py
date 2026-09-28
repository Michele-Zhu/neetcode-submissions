# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Sol 1:
# DFS, we visit the right child first, then left child
# each time we visit a right child we store when we reach that depth
# i.e. at d=0, we will first see the root
# d=1, the first element on the right will be stored

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        dfs(root, 0)
        return res