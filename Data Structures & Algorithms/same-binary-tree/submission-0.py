# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both empty
        if not p and not q:
            return True
        # one tree empty
        if not p or not q:
            False

        # BFS/level order traversal of the tree
        # FIFO queue containings tree depth to 
        # be parsed
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        while(q1 and q2):
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                # both nodes are empty
                if not nodeP and not nodeQ:
                    continue
                
                # one node empty or their value are distinct
                if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                    return False

                # nodes match continue the bfs
                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)
        return True
