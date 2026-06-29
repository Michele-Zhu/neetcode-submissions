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
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
                if val > 9:
                    carry = 1
                    val -= 10
                else:
                    carry = 0
                l1 = l1.next
                l2 = l2.next
                l3.next = ListNode(val)
                l3 = l3.next
            elif l1:
                val = l1.val + carry
                if val > 9:
                    carry = 1
                    val -= 10
                else:
                    carry = 0
                l1 = l1.next
                l3.next = ListNode(val)
                l3 = l3.next
            else:
                val = l2.val + carry
                if val > 9:
                    carry = 1
                    val -=10
                else:
                    carry = 0
                l2 = l2.next
                l3.next = ListNode(val)
                l3 = l3.next
        if carry != 0:
            l3.next = ListNode(carry)
            l3 = l3.next
        return dummy.next