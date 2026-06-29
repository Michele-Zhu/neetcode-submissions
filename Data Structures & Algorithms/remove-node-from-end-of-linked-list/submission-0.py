# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer solution
        dummy = ListNode(0, head)
        first, second = head, dummy
        for _ in range(n):
            first = first.next
        
        while first:
            first = first.next
            second = second.next

        # remove second is points exactly to the node to be eliminated
        second.next = second.next.next
        return dummy.next