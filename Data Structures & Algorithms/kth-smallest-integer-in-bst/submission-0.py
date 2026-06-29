# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We have a BST, with property:
        # 1. curr node value is between left and right child
        # If we find the leftmost descendant we find the node 
        # at k = 0 -> we can traverse the tree in-order with a 
        # DFS -> left child -> node -> right child
        # which guarantees to see the correct total ordering

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
            
        def dfs_optimal(node):
            if not node:
                return None
            # visit left
            left = dfs_optimal(node.left)
            # visit current and increment counts
            self.visited_count +=1
            if self.visited_count == k:
                self.result = node.val
            right = dfs_optimal(node.right)

        # In-order traversal
        # O(n), O(n)
        # arr = []
        # dfs(root)
        # return arr[k-1]

        # In-order optimized -> count the nodes as we traverse them
        # O(h+k), O(h) -> worst case is still O(n), when k=n
        self.visited_count = 0
        self.result = root.val
        dfs_optimal(root)
        print(self.result)
        return self.result
