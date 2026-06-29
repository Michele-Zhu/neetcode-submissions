# Definition for singly-linked list.
# class ListListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListListNode], l2: Optional[ListListNode]) -> Optional[ListListNode]:
        dummy = ListNode(0)
        l3 = dummy  # result
        carry = 0

        # Can I make this code more readable?
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            l3.next = ListNode(val)
            
            # Update the pointer
            l3 = l3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next