# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Iteration: We traverse the list to count the number of nodes
        # once we know the number of nodes we can remove the index N - n

        curr = head
        n_nodes = 0
        while curr:
            n_nodes += 1
            curr = curr.next
        
        # remove the first element
        remove_idx = n_nodes - n
        if remove_idx == 0: 
            return head.next

        curr = head
        for i in range(n_nodes - 1):
            if i+1 == remove_idx:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head