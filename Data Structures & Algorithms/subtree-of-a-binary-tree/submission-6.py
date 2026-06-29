# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Idea use bfs to search a common subroot
        # use dfs to check the match between trees
        # hint: there is a way to optimize this search?
        # using this search my solution would be O(m*n) and O(m+n) where 
        # m is #nodes in subroot and n #nodes in root

        def dfs_match(t1, t2):
            # This code returns true if two trees are the same

            # case t1 and t2 are different
            # t1 is none, t2 not none
            # t1 not none, t2 is none
            # t1.val != t2.val
            # if t1!=t2:
            #     return False
            # Both nodes are None return true
            if not t1 and not t2:
                return True
            ## One node is empty
            if (not t1 and t2) or (t1 and not t2):
                return False


            left = dfs_match(t1.left, t2.left)
            right = dfs_match(t1.right, t2.right)
            return (left and right) and t1.val == t2.val

        # BFS search to find a common ancestor
        # node need to use two queues
        q1 = deque()
        q1.append(root)
        visited_count = 0
        while(q1):
            for _ in range(len(q1)):
                node1 = q1.popleft()
                visited_count += 1

                # node emtpy move forward
                if not node1:
                    continue
                if node1.val == subRoot.val:
                    # print(f"entering matching process: {visited_count}")
                    is_subtree = dfs_match(node1, subRoot)
                    if is_subtree: return True
                    # else: 
                    #    print("match failed")
                    #    continue
                
                # append left and right childs to queue
                q1.append(node1.left)
                q1.append(node1.right)
        # print("safely ended the while loop")
        return False