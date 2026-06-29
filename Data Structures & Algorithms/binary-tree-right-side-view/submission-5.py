# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs_rightSideView(root):
            # This algorithm cost O(n) and O(n) space!
            # Can we do better? -> We always have to traverse all the tree
            # in best or worst case here!
            # -> intuitively DFS should be a better approach on average
            # -> actually the DFS solution is equal!
            # There is a way to prune the nodes?
            # -> not really if you only visit right you can miss some views
            if not root:
                return []

            q = deque()
            q.append(root)
            result = []

            while(q):
                same_level = []
                for _ in range(len(q)):
                    node = q.popleft()
                    same_level.append(node.val)

                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                result.append(same_level)
            
            for i in range(len(result)):
                result[i] = result[i][-1]
            
            return result
    
        def dfs_rightSideView(node, depth):
            if not node:
                return None
            # New depth encountered add the right val
            if depth == len(self.res):
                self.res.append(node.val)
            
            dfs_rightSideView(node.right, depth + 1)
            dfs_rightSideView(node.left, depth + 1)


        self.res = []
        dfs_rightSideView(root, 0)
        return self.res