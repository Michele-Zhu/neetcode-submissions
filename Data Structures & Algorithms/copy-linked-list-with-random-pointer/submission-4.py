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
        # HashMap Solution Two passes
        old_to_new = {None:None}

        curr = head
        while curr:
            new = Node(curr.val)
            old_to_new[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            new = old_to_new[curr]
            new.next = old_to_new[curr.next]
            new.random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]
        