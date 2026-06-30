# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tmp = l1.next
                head.next = l1
                l1.next = None
                l1 = tmp
                head = head.next
            elif l1.val > l2.val:
                tmp = l2.next
                head.next = l2
                l2.next = None
                l2 = tmp
                head = head.next
        
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        
        head = dummy.next
        dummy = None
        return head