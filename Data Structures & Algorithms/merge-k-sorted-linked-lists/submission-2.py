# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, l1: List[Optional], l2: List[OptionalListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy 

        # Question whats the cost here? O(n+m) time, O(1) space,
        #   where the n, m are sizes of l1 and l2 
        # Can you do better? -> nothing much, you could store either l1/l2 vals and skip
        # the pointers modifications, but this will reduce clarity of the code
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # Exe trace: [-4, -2, ..., 25], [-7], dummy = tail = ListNode(0)
        # l1.val >= l2.val, tmp = None, tail.next = -8, l2 = tmp = None
        # exit loop with tail = -8, tail.next = None
        # should enter 

        if l1:
            tail.next = l1
        if l2:
            # print(f"running")
            tail.next = l2

        tail = dummy.next
        dummy.next = None
        dummy = None
        return tail

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists
        # solution which is better than O(n * k), k total number of lists, n total number of nodes across all lists
        # if we provide a solution with heaps we have O(nlog n) cost, and space cost O(log n)
        # i.e. empty all the lists into the priority queue
        # Can we do better?
        # what if we use a circular index, each time inserting an element into the heap (priority queue)?
        # then popping is just calling heapq.heappop()
        # The problem with this approach is that you still need to guarantee the min behavior
        
        # Another approach is to merge the sorted lists two at time
        # do you remember how to do that?

        # Third case: else
        head = lists[0]
        for i in range(1, len(lists)):
            head = self.mergeTwoLists(head, lists[i])

        return head
        