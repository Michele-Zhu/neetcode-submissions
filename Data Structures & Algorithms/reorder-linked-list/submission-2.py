# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # using arr to support traversing

        nodes = []

        curr = head
        n_nodes = 0
        while curr:
            nodes.append(curr)
            n_nodes += 1
            curr = curr.next
        print(n_nodes)

        i, j = 0, n_nodes - 1
        while i < j:
            nodes[i].next = nodes[j]
            nodes[j].next = nodes[i+1]
            i += 1
            j -= 1
        nodes[i].next = None