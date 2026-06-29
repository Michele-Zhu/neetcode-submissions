# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return result