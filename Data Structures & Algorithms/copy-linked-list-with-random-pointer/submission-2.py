"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # 1. Iterate though the list, copy the node, make the new copy
        #    next point to the old node random, and make the old random point 
        #    to the new copy
        # 2. Iterate though the list, make the new copy random point to the correct
        #    random, the condition is l2.random = l2.next.random if l2.next else None
        # 3. Iterate though the list, fix the l1.random back to the correct one
        #    l1.random = l2.next
        #    Fix the copy next to the correct node with
        #    l2.next = l1.next.random if l1.next else None
        
        l1 = head
        while l1:
            l2 = Node(l1.val, l1.random, None)
            l1.random = l2
            l1 = l1.next

        newHead = head.random
        l1 = head
        while l1:
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None
            l1 = l1.next
        
        l1 = head
        while l1:
            l2 = l1.random
            l1.random = l2.next
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next
        return newHead