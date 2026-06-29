from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list1 = head
        list2 = slow.next
        slow.next = None
        # reverse the second list
        prev, curr = None, list2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        list2 = prev
        # Now list2 contains [8, 6]

        hi = list2
        while hi:
            print(hi.val)
            hi = hi.next 
        print()
        
        hi = list1
        while hi:
            print(hi.val)
            hi = hi.next 
        print()
        head = list1
        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2