"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
# Simple deep copy when there are no pointers
dummy = Node(0)
tail, curr = dummy, head

while(curr):
    new_node = Node(curr.val)
    tail.next = new_node
    tail = tail.next
    curr = curr.next
tail.next = None

return dummy.next

# removing dummy node
if not head:
    return None

new_head = (Node(head.val))
old_curr = head.next
new_curr = new_head

while old_curr:
    new_curr.next = Node(old_curr.val)
    new_curr = new_curr.next
    old_curr = old_curr.next
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: 
            return None
        
        # Copy the nodes in the initial list
        # set new node random to random address
        # store into the initial list.random the new node address 
        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.random 
            l1.random = l2
            l1 = l1.next

        # Fix the new list random pointers to the correct ones
        new_head = head.random
        l1 = head
        while l1:
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None
            l1 = l1.next
        
        # Fix the pointers to next node of copied nodes
        # and the old list
        l1 = head
        while l1 is not None:
            l2 = l1.random 
            l1.random = l2.next 
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next
        
        return new_head